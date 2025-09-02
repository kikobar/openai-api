from config import *
import requests
import sys

def retrieve_item(conversation,message):
    url = base_url+"conversations/"+conversation+"/items/"+message

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.json()["content"][0]["text"])


if __name__ == '__main__':
    retrieve_item(str(sys.argv[1]),str(sys.argv[2]))
