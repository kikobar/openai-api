from config import *
import requests
import sys

def delete_file(file_id):
    url = base_url+"files/"+file_id

    payload = {}
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    delete_file(str(sys.argv[1]))
