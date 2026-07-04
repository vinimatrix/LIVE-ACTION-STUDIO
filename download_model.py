from huggingface_hub import hf_hub_download

print("Iniciando descarga de checkpoint. Esto tomará unos momentos (4GB)...")
hf_hub_download(
    repo_id="runwayml/stable-diffusion-v1-5", 
    filename="v1-5-pruned-emaonly.safetensors", 
    local_dir="C:/Users/vm004458/Documents/ComfyUI/models/checkpoints"
)
print("¡Descarga de modelo exitosa!")
