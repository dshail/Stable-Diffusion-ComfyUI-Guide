#This script automates downloading and placing the Stable Diffusion model in the correct directory.
import os
import requests

def download_model(url, output_path):
    """Downloads the model checkpoint if it does not exist."""
    if not os.path.exists(output_path):
        print(f"Downloading model from {url}...")
        response = requests.get(url, stream=True)
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print("Model download complete.")
    else:
        print("Model already exists.")

# Define model URL and target path
model_url = "https://huggingface.co/path-to-model"
model_path = "ComfyUI/models/checkpoints/v1-5-pruned-emaonly-fp16.ckpt"

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# Download the model
download_model(model_url, model_path)
