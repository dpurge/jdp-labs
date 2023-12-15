# CodeLlama served by VLLM

Install [container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Test if docker has access to GPU:

```sh
docker run -it --rm --gpus all ubuntu nvidia-smi
```

Error: Rancher Desktop does not have access to the GPU!

Received error with NVIDIA drivers 511.65 and CUDA 11.6 on NVIDIA GeForce RTX 3070 Laptop GPU: `nvidia-container-cli: requirement error: unsatisfied condition: cuda>=12.1`

Upgraded NVIDIA drivers to [528.49](https://pl.download.nvidia.com/Windows/528.49/528.49-notebook-win10-win11-64bit-international-dch-whql.exe)

This reports CUDA 12.0 and container still fails to start: `unsatisfied condition: cuda>=12.1`

Upgraded CUDA to [12.2.0](https://developer.download.nvidia.com/compute/cuda/12.2.0/local_installers/cuda_12.2.0_536.25_windows.exe)

`codellama/CodeLlama-7b-hf` does not fit into my GPU, I had to try `casperhansen/vicuna-7b-v1.5-awq`

It works:

```sh
docker compose up

curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "casperhansen/vicuna-7b-v1.5-awq","prompt": "San Francisco is a","max_tokens": 7,"temperature": 0}'

{"id":"cmpl-ad5c580e7f5e4b6cbbdb0bc8e7afd5ff","object":"text_completion","created":2145,"model":"casperhansen/vicuna-7b-v1.5-awq","choices":[{"index":0,"text":" city in California, United States.","logprobs":null,"finish_reason":"length"}],"usage":{"prompt_tokens":5,"total_tokens":12,"completion_tokens":7}}
```
