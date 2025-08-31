from config import *
import requests
import sys

def delete_model_response(response):
    url = base_url+"responses/"+response

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    delete_model_response(str(sys.argv[1]))
