from config import *
import requests
import sys

def list_vector_store_files(vector_store):
    url = base_url+"vector_stores/"+vector_store+"/files"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    list_vector_store_files(str(sys.argv[1]))
