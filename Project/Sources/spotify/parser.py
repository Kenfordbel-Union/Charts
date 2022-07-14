import base64
import json
import requests
from secrets import *
cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'
# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{cid}:{secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint

playlistId = "37i9dQZEVXbNG2KDcFcKOF"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(res.json(), indent=2))

