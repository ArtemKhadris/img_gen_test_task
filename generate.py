import torch
from diffusers import (
    StableDiffusionXLPipeline,
    DPMSolverMultistepScheduler
)
from config import MODEL_ID, DEFAULT_CONFIG, SAVING_NAME


def generate_image(
    prompt: str = DEFAULT_CONFIG["prompt"],
    steps: int = DEFAULT_CONFIG["steps"],
    cfg_scale: float = DEFAULT_CONFIG["cfg_scale"],
    width: int = DEFAULT_CONFIG["width"],
    height: int = DEFAULT_CONFIG["height"],
    seed: int | None = DEFAULT_CONFIG["seed"],
):
    """
    Generate an image using an SDXL-based PixelWave model.

    The model is loaded from a single .safetensors checkpoint,
    which allows reuse of the same weights as in ComfyUI / A1111.

    Args:
        prompt (str): Positive text prompt
        steps (int): Number of denoising steps
        cfg_scale (float): Classifier-Free Guidance scale
        width (int): Output image width
        height (int): Output image height
        seed (int | None): Random seed for reproducibility

    Returns:
        PIL.Image.Image: Generated image
    """

    # Load SDXL pipeline from a single-file checkpoint
    # torch_dtype=float16 is critical for SDXL to reduce VRAM usage
    pipe = StableDiffusionXLPipeline.from_single_file(
        MODEL_ID,
        torch_dtype=DEFAULT_CONFIG["torch_dtype"],
        use_safetensors=True,
        variant="fp16",
    )

    # Replace default scheduler with DPM++ 2M Karras equivalent
    # This closely matches popular samplers used in ComfyUI / A1111
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(
        pipe.scheduler.config,
        use_karras_sigmas=True
    )

    # Move pipeline to GPU
    pipe = pipe.to(DEFAULT_CONFIG["device"])

    # Optional memory optimizations for SDXL
    pipe.enable_attention_slicing()

    # Set random generator for reproducibility if seed is provided
    generator = None
    if seed is not None:
        generator = torch.Generator(device=DEFAULT_CONFIG["device"]).manual_seed(seed)

    # Run inference
    result = pipe(
        prompt=prompt,
        negative_prompt=DEFAULT_CONFIG["negative_prompt"],
        num_inference_steps=steps,
        guidance_scale=cfg_scale,
        width=width,
        height=height,
        generator=generator,
    )

    # SDXL pipeline returns a list of images
    return result.images[0]


if __name__ == "__main__":
    # Simple entry point for manual testing
    image = generate_image()
    image.save(SAVING_NAME)