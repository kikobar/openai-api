from config import *
import requests
import json
import sys

def update_conversation(conversation,metadata):
    url = base_url+"conversations/"+conversation

    payload = json.dumps({
      "metadata": json.loads(metadata)
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    update_conversation(str(sys.argv[1]),str(sys.argv[2]))
