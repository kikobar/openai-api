from config import *
import requests
import json
import sys
import base64
from PIL import Image
from io import BytesIO
from datetime import datetime

def create_image(model,prompt):
    url = base_url+"images/generations"

    payload = json.dumps({
      "prompt": prompt,
      "model": model
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }
    date_time_string = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    response = requests.request("POST", url, headers=headers, data=payload)
    decoded_bytes = base64.b64decode(response.json()["data"][0]["b64_json"])
    byte_stream = BytesIO(decoded_bytes)
    image = Image.open(byte_stream)
    image.save("./output_images/output-"+date_time_string+".png", "PNG")

    print("Image ./output_images/output-"+date_time_string+".png has been generated.")


if __name__ == '__main__':
    create_image(str(sys.argv[1]),str(sys.argv[2]))
