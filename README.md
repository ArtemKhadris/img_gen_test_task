# Image generation test task

# Step 1 - Launching the model

The model is launched on a Windows system, ComfyUI is used as the UI, and [PixelWave](https://civitai.com/models/141592/pixelwave) (a fine-tuned version of the Flux model) was chosen as the model.
To run the model, you also need [VAE](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/ae.safetensors), [T5xxl](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors) and [CLIP L](https://huggingface.co/stabilityai/stable-diffusion-3-medium/blob/main/text_encoders/clip_l.safetensors) (a hugging face account is required for access and download).

After downloading all the models, you need to use the console to enter the folder where the environment will be downloaded.
While in the desired folder, run the command ```git clone https://github.com/comfyanonymous/ComfyUI.git``` to download ComfyUI. Then, navigate to the folder itself using ```cd ComfyUI```.
While in the folder, create a Python environment: ```python -m venv test_venv``` and activate it for Mac/Linux: ```source venv/bin/activate``` or for Windows: ```venv\Scripts\activate```. Then install the necessary packages with ```pip install -r requirements.txt```.
The UI was launched using the command ```python main.py --lowvram --use-pytorch-cross-attention --async-offload```

The workflow used is ```trial_wf.json```.

Main model shold be located in ```...ComfyUI\models\diffusion_models```, VAE model should be located in ```...ComfyUI\models\vae```, and T5xxl & CLIP L should be located in ```...ComfyUI\models\text_encoders```.

Results:

1) Prompt: ```A dramatic seascape captures two solitary figures standing resolutely atop rugged cliffs, their silhouettes sharply defined against a tempestuous sky filled with swirling storm clouds, streaked with flashes of jagged lightning. The air is thick with the scent of salt and impending rain, as heavy winds whip around them, tousling their hair and clothing. Below, the churning sea roars with chaotic waves, its frothy crests catching glimpses of pale moonlight, reflecting the turmoil within the pair. Their postures convey a profound sense of longing and resolve, as they gaze toward the horizon, suggesting an unspoken bond amidst nature's fury. This scene exudes a cinematic lighting quality, evoking both drama and emotion in its breathtaking, high-contrast palette. they stand at a physical and emotional distance from one another. detailed```
   
   Seed: ```36889128122473```
   
   Steps: ```8```
   
   Sampler: ```euler```
   
   Res: ```832x1216```
   
   Pic:
   
   <img width="832" height="1216" alt="pws4_00002_" src="https://github.com/user-attachments/assets/6a486d0a-f5a5-4622-97ad-bdc8580effdd" />

3) Prompt: ```oil painting, rough, textural, broad brush strokes, portrait of a stunning skeleton pirate, tricorne hat, bandana, holding flintlock musket, standing on deck of burning ship```

   Seed: ```7432956701536```

   Steps: ```15```

   Sampler: ```euler```

   Res: ```1024x1024```

   Pic:
   
   <img width="1024" height="1024" alt="pws4_00003_" src="https://github.com/user-attachments/assets/b21e9d5c-5c44-4f8d-b2c0-b477b0a6eb45" />

4) Prompt: ```Create a romantic closeup image of a big white old sailing Ship that is sailing in clouds. The sailcloths are Made of Clouds. sunrise, ship breakes the surface of shimmering,clouds. The atmosphere is dreamy and magical, with a look reminiscent of animated films. Breathtaking sunrise scene, shadows, fantasy, natural lighting, dreamlike, surreal, sharp focus, detailed, cinematic, trending on ArtStation, double exposure, fantastic, splash art, detailed, hyper-detailed, maximalist style, concept art, mysterious glow, dynamic lighting, superb composition, finest details, mystical glow, best quality, sharp focus, high contrast, stylized, clear, colorful, highest quality, anime, cyberpunk, masterpiece, award-winning, anime, cyberpunk, DB4RZ, DB4RZ style painting, in the style of cksc```
   
   Seed: ```642092123```

   Steps: ```20```

   Sampler: ```euler```

   Res: ```2048x2048```

   Pic:

   <img width="2048" height="2048" alt="pws4_00005_" src="https://github.com/user-attachments/assets/5a8124a0-f059-4f08-840a-da9abe48c9f8" />

# Step 2 - Python Mini Pipeline

In the second step we will also use PixelWave, but this will be the [fine-tuned version of SDXL](https://civitai.com/models/141592?modelVersionId=716090). Model shold be located in ```...\ComfyUI\models\diffusion_models``` folder

We will use the same environment that ComfyUI provided us, we only need to add ```pip install diffusers```.

All generation settings are specified in the ```config.py``` file. The image generation itself is performed using ```generate.py``` (don't forget to change the path to the saved image).
The FULL SYSTEM PATH must be specified for the model to work correctly on Windows.

Image generated with the settings specified in the config:

<img width="1024" height="1024" alt="result" src="https://github.com/user-attachments/assets/65cc9284-31f3-49de-a34f-b2962656e73d" />

# Step 3 - Jypiter notepad

The notebook (```generate.ipynb```) is similar to the code from step 2. To run the notebook, you need to complete the installation from step 1 and step 2, and download the model and place it in the path specified in step 2.

# Step 4 - Description of the experience

## Practical experience with diffusion ecosystem tools

I have hands-on experience with the following technologies:

LoRA (Low-Rank Adaptation) — prepared datasets, trained LoRA adapters for different Stable Diffusion–based models (including SD 1.5 and SDXL), and integrated them into inference pipelines. I have worked with prompt tuning, weight scaling, and quality evaluation for style consistency.

ControlNet — built and used pipelines with various ControlNet models (pose, depth, lineart, etc.), including data preparation, conditioning setup, and integration into both ComfyUI workflows and custom pipelines.

DreamBooth / fine-tuning — have experience preparing training data and running fine-tuning experiments to adapt base models to specific styles, with attention to overfitting and generalization.

ComfyUI / Automatic1111 — actively used both interfaces for experimentation, parameter tuning, debugging generation issues, and building reusable workflows. ComfyUI was primarily used for flexible, node-based pipeline construction, while Automatic1111 was used for rapid iteration and testing.

## Key considerations for deploying an internal image generation service

When launching a diffusion-based image generation service inside a company, several key aspects must be considered.

First, data and licensing are critical: it is important to clearly understand the licenses of base models, fine-tuned checkpoints, LoRAs, and datasets, and to ensure that generated content can be legally used for commercial or internal purposes. (As you can see, one of the generated images has a link to a website at the bottom, but this website does not exist, so you need to keep an eye on this too.)

Second, performance and stability matter for daily usage. This includes predictable inference times, proper error handling, and safeguards against model crashes or out-of-memory issues, especially when multiple users access the system simultaneously.

Third, infrastructure and GPU resources must be planned carefully. SDXL-class models require sufficient VRAM, and scaling strategies (multiple GPUs, job queues, batching, or mixed precision) should be considered to balance cost and throughput.

Finally, usability for the team is essential. Non-technical users benefit from simple interfaces, clear presets, and reproducible results, while technical users need transparency, configurability, and the ability to debug or extend pipelines without friction.

A successful internal service balances technical robustness with ease of use, enabling teams to focus on creative tasks rather than tooling complexity.
