from config import *
import requests
import sys

def delete_conversation(conversation):
    url = base_url+"conversations/"+conversation

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
    
if __name__ == '__main__':
    delete_conversation(str(sys.argv[1]))
