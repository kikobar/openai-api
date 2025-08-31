from config import *
import requests
import sys

def retrieve_model_response(response):
    url = base_url+"responses/"+response

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    retrieve_model_response(str(sys.argv[1]))
