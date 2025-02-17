#This script loads the model and generates images based on text prompts.

import comfyui

def generate_image(prompt, steps=50, output_path="output.png"):
    """Generates an image using the Stable Diffusion model in ComfyUI."""
    model = comfyui.load_model("ComfyUI/models/checkpoints/v1-5-pruned-emaonly-fp16.ckpt")
    image = model.generate(prompt, steps=steps)
    image.save(output_path)
    print(f"Image saved at {output_path}")

if __name__ == "__main__":
    prompt = input("Enter your text prompt: ")
    generate_image(prompt)
