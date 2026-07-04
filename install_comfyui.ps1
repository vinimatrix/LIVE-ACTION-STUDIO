$ErrorActionPreference = "Stop"

$ComfyPath = "C:\Users\vm004458\Documents\ComfyUI"

if (Test-Path $ComfyPath) {
    Write-Host "Limpiando directorio antiguo defectuoso..."
    Remove-Item $ComfyPath -Recurse -Force
}

Write-Host "Clonando repositorio ComfyUI de forma limpia..."
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git $ComfyPath
Set-Location $ComfyPath

Write-Host "Creando entorno virtual..."
python -m venv venv
$PythonVenv = ".\venv\Scripts\python.exe"

Write-Host "Instalando dependencias (puede tardar un momento)..."
& $PythonVenv -m pip install --upgrade pip
& $PythonVenv -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
& $PythonVenv -m pip install -r requirements.txt
& $PythonVenv -m pip install huggingface_hub

Write-Host "Descargando modelo base de prueba (v1.5) usando huggingface-cli para evitar fallos de conexión..."
& $PythonVenv -m huggingface_hub.commands.huggingface_cli download runwayml/stable-diffusion-v1-5 v1-5-pruned-emaonly.safetensors --local-dir models\checkpoints

Write-Host "¡Instalación exitosa! Puedes iniciar ComfyUI ejecutando: $PythonVenv main.py --cpu"
