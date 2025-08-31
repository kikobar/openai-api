from config import *
import requests

url = base_url+"files"

payload = {}
headers = {
  'Authorization': 'Bearer '+secret_key,
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

