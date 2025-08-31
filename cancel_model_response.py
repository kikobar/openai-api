from config import *
import requests
import sys

def cancel_model_response(response):
    url = base_url+"responses/"+response+"/cancel"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    cancel_model_response(str(sys.argv[1]))
