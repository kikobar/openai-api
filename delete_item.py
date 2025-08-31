from config import *
import requests
import sys

def delete_item(conversation,item):
    url = base_url+"conversations/"+conversation+"/items/"+item

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    delete_item(str(sys.argv[1]),str(sys.argv[2]))
