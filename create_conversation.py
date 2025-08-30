from config import *
import requests

url = base_url+"conversations"

payload = {}
headers = {
  'Authorization': 'Bearer '+secret_key
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
