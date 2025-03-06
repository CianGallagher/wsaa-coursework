import requests
import json
from config import apikeys as cfg
import base64

#https://docs.github.com/en/rest/guides

# url = 'https://api.github.com/repos/CianGallagher/PrivateRepo'
file_url = "https://api.github.com/repos/CianGallagher/PrivateRepo/contents/andrew.txt"

apikey = cfg['github_private_repo_key']

# Request the data from the API using the URL and API key
response = requests.get(file_url, auth=('token', apikey))

print(response.status_code)

# Dump the response to a JSON file called private_repo.json
filename = "private_repo.json"
with open(filename, 'w') as f:
    json.dump(response.json(), f, indent=4)

file_data = response.json()
content = response.json()['content']
print(content)

# GitHub API encodes txt in Base64, this seems to be a standard encoding that github API uses when reading to JSON - https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28 & https://docs.python.org/3/search.html?q=.b64decode
# Decode the content from Base64 to a string
decoded_content = base64.b64decode(content).decode('utf-8')
print(decoded_content)

# Update the content of the file per the assignment instructions
updated_content = decoded_content.replace("Andrew", "Cian")
print(updated_content)

# Re-encode the updated content to Base64
re_encoded_content = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')
print(re_encoded_content)

# Create a JSON object with the new content and the SHA of the file, the sha in this case is conveniently in the file metadata - https://stackoverflow.com/questions/11801983/how-to-create-a-commit-and-push-into-repo-with-github-api-v3
commit_json = {
    "message": "Replace the string Andrew with the string Cian",  # Commit message
    "content": re_encoded_content,                                
    "sha": file_data['sha']                                     
}
# Commit the changes to the file - https://www.geeksforgeeks.org/put-method-python-requests/
update_response = requests.put(file_url, auth=('token', apikey), json=commit_json)

print(update_response.status_code)
