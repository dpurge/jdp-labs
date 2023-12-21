# Local testing of vLLM

This is running in Ubintu WSL2 under Windows.

My python:

```sh
python3 --version
Python 3.10.12
```

Create and enter python virtual environment:

```sh
python3 -m venv /var/venv/vllm
source /var/venv/vllm/bin/activate
```

My GPU:

```sh
nvidia-smi
Thu Dec 21 19:58:27 2023
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.54.04              Driver Version: 536.25       CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3070 ...    On  | 00000000:01:00.0 Off |                  N/A |
| N/A   30C    P0              23W /  85W |      0MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

Install torch and vLLM:

```sh
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install vllm
```

Start vLLM:

```sh
python -m vllm.entrypoints.openai.api_server --model TheBloke/Llama-2-7B-AWQ --dtype half --served-model-name llama2-7b --trust-remote-code
(...snip...)
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Configure `Continue` extension to talk to the model:

```json
{
    "title": "Llama2-7b-vllm",
    "provider": "openai-aiohttp",
    "model": "llama2-7b",
    "api_base": "http://localhost:8000"
}
```

It starts, but hangs after a few generated tokens.
