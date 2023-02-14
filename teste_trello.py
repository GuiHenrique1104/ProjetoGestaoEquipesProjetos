import requests
import json

# retorna as pranchas (boards)

apiKey = '13a45376e8770f8efe9450e0974de27d'
apiToken = 'ATTAef2ff1e1acbc3e69e1128b6cc6179afec94c7a2c5d49abb165a277602f335574CFF83B61'

url = f"https://api.trello.com/1/members/me/boards?fields=name,url&key={apiKey}&token={apiToken}"

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
