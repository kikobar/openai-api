from config import *
import requests
import json
import sys

def create_text_item(conversation,message):
    url = base_url+"conversations/"+conversation+"/items"

    payload = json.dumps({
      "items": [
        {
          "type": "message",
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": message
            }
          ]
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    create_text_item(str(sys.argv[1]),str(sys.argv[2]))
