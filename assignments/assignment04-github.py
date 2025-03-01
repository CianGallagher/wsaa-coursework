#from github import Github
# import requests
# import urllib.parse
from config import apikeys

# 1. Access and Pull the repo file ?? Read more into authentication

# 2. Update the files text
with open("whatever the repo file is", "r") as file:
    content = file.read()

updated_content = content.replace("Andrew", "Cian")

# 3. Push the updated file back to the repo