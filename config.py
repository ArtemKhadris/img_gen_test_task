from pathlib import Path
import torch

# Path to SDXL-based PixelWave checkpoint in safetensors format
# Using absolute path to avoid ambiguity on Windows
MODEL_ID = Path(
    r"D:\stablediffusion\ComfyUI\models\diffusion_models\pixelwave_sdxl11.safetensors"
)

SAVING_NAME = "result.png"

# Default configuration for image generation
DEFAULT_CONFIG = {
    # Main positive prompt used for generation
    "prompt": (
        "anime style female character, detailed illustration, "
        "soft lighting, expressive eyes, high quality"
    ),

    # Negative prompt to suppress common diffusion artifacts
    "negative_prompt": (
        "low quality, blurry, extra fingers, bad anatomy, "
        "deformed hands, poorly drawn face"
    ),

    # Diffusion parameters
    "steps": 30,            # Number of denoising steps
    "cfg_scale": 7.0,       # Classifier-Free Guidance scale
    "width": 1024,          # Output image width (SDXL native)
    "height": 1024,         # Output image height (SDXL native)

    # Random seed for reproducibility (set to None for random behavior)
    "seed": 42,

    # Sampler / scheduler configuration
    "scheduler": "dpmpp_2m_karras",

    # Runtime configuration
    "torch_dtype": torch.float16,
    "device": "cuda"
}