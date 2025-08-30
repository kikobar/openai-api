from config import *
import requests
import sys

def list_items(conversation):
    url = base_url+"conversations/"+conversation+"/items"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    list_items(str(sys.argv[1]))
