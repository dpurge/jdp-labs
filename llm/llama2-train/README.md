# Fine-tune Llama-2

- LoRA = Low Rank Adaptation
- QLoRA = Quantized LoRA
- PEFT = Parameter Efficient Fine Tuning
- VRAM = Video RAM

Quantization = decreasing the precision of weigths to save VRAM (7B of parameters in 32 bits = 28GB vs. 7B of parameters in 4 bits = 3.5 GB)

## Virtual environment

- https://www.youtube.com/watch?v=OQdp-OeG1as
- https://github.com/jllllll/bitsandbytes-windows-webui

```pwsh
python -m venv C:/jdp/dat/venv/llm
C:/jdp/dat/venv/llm/Scripts/Activate.ps1
python.exe -m pip install --upgrade pip
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

## Run training

```pwsh
C:/jdp/dat/venv/llm/Scripts/Activate.ps1
python train.py
```