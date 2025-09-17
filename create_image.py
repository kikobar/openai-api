from config import *
import requests
import json
import sys
import base64
from PIL import Image
from io import BytesIO
from datetime import datetime

def create_image(model,prompt,image_path=None):
    # choose endpoint depending on whether an image is provided
    if image_path:
        url = base_url+"images/edits"
    else:
        url = base_url+"images/generations"

    headers = {
      'Authorization': 'Bearer '+secret_key,
    }
    date_time_string = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    if image_path:
        # For edits, use multipart/form-data
        data = {
            "prompt": prompt,
            "model": model
        }
        files = {
            "image": open(image_path, "rb")
        }
        response = requests.post(url, headers=headers, data=data, files=files)
    else:
        # For generations, use JSON
        payload = json.dumps({
            "prompt": prompt,
            "model": model
        })
        headers['Content-Type'] = 'application/json'
        response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        sys.exit(1)
    # handle response data: both generation and edits return b64_json in data[0]
    decoded_bytes = base64.b64decode(response.json()["data"][0]["b64_json"])
    byte_stream = BytesIO(decoded_bytes)
    image = Image.open(byte_stream)
    image.save("./output_images/output-"+date_time_string+".png", "PNG")

    print("Image ./output_images/output-"+date_time_string+".png has been generated.")


if __name__ == '__main__':
    # usage: python create_image.py <model> <prompt> [image_path]
    model = str(sys.argv[1]) if len(sys.argv) > 1 else ''
    prompt = str(sys.argv[2]) if len(sys.argv) > 2 else ''
    image_path = str(sys.argv[3]) if len(sys.argv) > 3 else None
    create_image(model,prompt,image_path)
