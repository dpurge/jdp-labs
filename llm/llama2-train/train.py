import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
    TextStreamer)
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model, PeftModel
from datasets import load_dataset

if torch.cuda.is_available():
    device = 'cuda'
    for i in range(torch.cuda.device_count()):
        print(f"{i} = {torch.cuda.get_device_name(i)}")
else:
    device = 'cpu'

print(f"Running on device: {device}")

# Load the model

model_id = "Trelis/Llama-2-7b-chat-hf-sharded-bf16"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})

# Set up for training

def print_trainable_parameters(model):
    """
    Prints the number of trainable parameters in the model.
    """
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
    )

model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

config = LoraConfig(
    r=8,
    lora_alpha=32,
    # target_modules=["query_key_value"],
    target_modules=["self_attn.q_proj", "self_attn.k_proj", "self_attn.v_proj", "self_attn.o_proj"], # specific to Llama
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)
print_trainable_parameters(model)

# Data Setup

data = load_dataset("Abirate/english_quotes")
data = data.map(lambda samples: tokenizer(samples["quote"]), batched=True)

# Training

tokenizer.pad_token = tokenizer.eos_token

trainer = Trainer(
    model=model,
    train_dataset=data["train"],
    args=TrainingArguments(
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        warmup_steps=2,
        max_steps=10,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=1,
        output_dir="outputs",
        optim="paged_adamw_8bit"
    ),
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False  # silence the warnings
trainer.train()

# Inference

def stream(user_prompt):
    runtimeFlag = "cuda:0"
    system_prompt = 'You are a helpful assistant that provides accurate and concise responses'

    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

    prompt = f"{B_INST} {B_SYS}{system_prompt.strip()}{E_SYS}{user_prompt.strip()} {E_INST}\n\n"

    inputs = tokenizer([prompt], return_tensors="pt").to(runtimeFlag)

    streamer = TextStreamer(tokenizer)

    # Despite returning the usual output, the streamer will also print the generated text to stdout.
    _ = model.generate(**inputs, streamer=streamer, max_new_tokens=500)

model.config.use_cache = True # re-enable warnings
model.eval()

stream('Provide a very brief comparison of salsa and bachata.')

# Push Model to Hub
base_model_name = model_id.split("/")[-1]
adapter_model = f"DPurge/{base_model_name}-fine-tuned-adapters"

# model.save_pretrained(adapter_model, push_to_hub=True, use_auth_token=True)
# model.push_to_hub(adapter_model, use_auth_token=True)
model.save_pretrained(adapter_model, push_to_hub=False, use_auth_token=False)

# reload the base model - this is loading the full original model, not quantized
model = AutoModelForCausalLM.from_pretrained(model_id, device_map='cpu', trust_remote_code=True, torch_dtype=torch.float16)

model = PeftModel.from_pretrained(
    model,
    adapter_model,
)

model = model.merge_and_unload() # merge adapters with the base model.
# model.push_to_hub(new_model, use_auth_token=True, max_shard_size="5GB")

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
# tokenizer.push_to_hub(new_model, use_auth_token=True)
