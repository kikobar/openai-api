from config import *
import requests
import sys

def retrieve_conversation(conversation):
    url = base_url+"conversations/"+conversation

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    retrieve_conversation(str(sys.argv[1]))
