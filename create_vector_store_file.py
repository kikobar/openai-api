from config import *
import requests
import json
import sys

def create_vector_store_file(vector_store_id,file_id):
    url = base_url+"vector_stores/"+vector_store_id+"/files"

    payload = json.dumps({
      "file_id": file_id
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    create_vector_store_file(str(sys.argv[1]),str(sys.argv[2]))
