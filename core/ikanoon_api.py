import requests
from dotenv import dotenv_values
config = dotenv_values(".env")

query = "Indian Penal Code"
pagenum = 0
doctype = "laws" # as specified by the API
API_TOKEN = config["IKANOON_API_KEY"]
#encoded_api_token = b64encode(API_TOKEN.encode()).decode()
#encoded_api_token = b64encode(API_TOKEN.encode('ascii')).decode('ascii')
URL = f"https://api.indiankanoon.org/search/?formInput={query}&pagenum={pagenum}&doctypes={doctype}"


DOC_ID = "148853451"
DOC_URL = f"https://api.indiankanoon.org/doc/{DOC_ID}/" #too lengthy, 25k words
headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Accept": "application/json"
}

response = requests.post(DOC_URL, headers=headers)
print(response.json())


