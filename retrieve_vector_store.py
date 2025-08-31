from config import *
import requests
import sys

def retrieve_vector_store(vector_store):
    url = base_url+"vector_stores/"+vector_store

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    retrieve_vector_store(str(sys.argv[1]))
