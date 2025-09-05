from config import *
import requests
import json
import sys

def create_model_response(conversation,model,message):
    url = base_url+"responses"

    payload = json.dumps({
      "model": model,
      "tools": [
      {"type": "web_search"},
      {"type": "file_search", "vector_store_ids" :vector_store}
      ],
      "input": message,
      "conversation": conversation
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.json()["output"][-1]["content"][0]["text"])

if __name__ == '__main__':
    create_model_response(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
