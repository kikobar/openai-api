from config import *
import requests
import sys

def retrieve_vector_store_file_content(vector_store,file_id):
    url = base_url+"vector_stores/"+vector_store+"/files/"+file_id+"/content"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    retrieve_vector_store_file_content(str(sys.argv[1]),str(sys.argv[2]))
