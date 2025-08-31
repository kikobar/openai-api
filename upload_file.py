from config import *
import requests
import sys

def upload_file(filename, path):
    url = base_url+"files"

    payload = {'purpose': 'user_data'}
    files=[
      ('file',(filename,open(path,'rb'),'application/pdf'))
    ]
    headers = {
      'Authorization': 'Bearer '+secret_key,
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


if __name__ == '__main__':
    upload_file(str(sys.argv[1]),str(sys.argv[2]))
