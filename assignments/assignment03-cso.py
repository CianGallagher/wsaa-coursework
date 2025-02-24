import requests
import json

CSO_URL = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = requests.get(CSO_URL)
data = response.json()

with open("cso.json", "w") as f:
    json.dump(data, f)