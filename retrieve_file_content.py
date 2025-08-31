from config import *
import requests
import sys

def retrieve_file_content(file_id):
    url = base_url+"files/"+file_id+"/content"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    retrieve_file_content(str(sys.argv[1]))
