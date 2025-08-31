from config import *
import requests
import json
import sys

def update_vector_store_file(vector_store_id,file_id,attributes):
    url = base_url+"vector_stores/"+vector_store_id+"/files/"+file_id

    payload = json.dumps({
      "attributes": json.loads(attributes)
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    update_vector_store_file(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
