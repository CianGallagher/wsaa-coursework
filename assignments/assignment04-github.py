import requests
import json
from config import apikeys as cfg

url = 'https://api.github.com/repos/CianGallagher/PrivateRepo'

apikey = cfg['github_private_repo_key']

# Request the data from the API using the URL and API key
response = requests.get(url, auth=('token', apikey))

print(response.status_code)

filename = "private_repo.json"
with open(filename, 'w') as f:
    json.dump(response.json(), f, indent=4)