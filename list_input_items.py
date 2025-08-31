from config import *
import requests
import sys

def list_input_items(response):
    url = base_url+"responses/"+response+"/input_items"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    list_input_items(str(sys.argv[1]))
