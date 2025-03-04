import requests
import json
from config import apikeys as cfg

# url = 'https://api.github.com/repos/CianGallagher/PrivateRepo'
contents_url = "https://api.github.com/repos/CianGallagher/PrivateRepo/contents/andrew.txt"

apikey = cfg['github_private_repo_key']

# Request the data from the API using the URL and API key
response = requests.get(contents_url, auth=('token', apikey))

print(response.status_code)

filename = "private_repo.json"
with open(filename, 'w') as f:
    json.dump(response.json(), f, indent=4)

# Find a way to interact with the andrew.txt file within this repo.
# Content in the JSON output is stated as "content": "QW5kcmV3Cg==\n", not sure what language this is.