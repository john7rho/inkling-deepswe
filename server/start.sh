#!/bin/bash
# Inkling 2 Mini (Q4_K_M) on the RTX 4080 via llama.cpp, OpenAI-compatible API.
# Listens on 127.0.0.1:8080 (host) and 192.168.122.1:8080 and :80 (libvirt VMs and Docker networks; port 80
# is for the DeepSWE sandbox proxy, which only allows 80/443). Bearer key is in ~/inkling/api-key.
# Keep -c 65536 -np 1 -b 32 -ub 32 --fit-target 256 (verified on a 57K-token prompt; start.sh.32k is the old
# 32K/batch-64 config, which reads prompts ~1.7x faster): with a larger batch llama.cpp splits the model between
# GPU and RAM, and that split returns NaN garbage on prompts longer than a few dozen tokens.
docker rm -f inkling-server >/dev/null 2>&1
docker run -d --restart unless-stopped --gpus all --name inkling-server \
  -p 127.0.0.1:8080:8080 -p 192.168.122.1:8080:8080 -p 192.168.122.1:80:8080 -v $HOME/inkling:/work:ro \
  nvidia/cuda:12.8.1-devel-ubuntu22.04 /work/llama.cpp/build/bin/llama-server \
  -m /work/models/Inkling-2-Mini-Q4_K_M.gguf --host 0.0.0.0 --port 8080 --jinja --alias inkling-2-mini \
  --api-key-file /work/api-key -c 65536 -np 1 -b 32 -ub 32 --fit-target 256 --no-reasoning-preserve
