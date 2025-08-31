from config import *
import requests
import json
import sys

def modify_vector_store(vector_store_id,metadata):
    url = base_url+"vector_stores/"+vector_store_id

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
    modify_vector_store(str(sys.argv[1]),str(sys.argv[2]))
