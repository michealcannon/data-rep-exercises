import requests
import json

apiKey = "3c1cd1cbc4b72b33b06c51a3d4d38fb10d41c76-2"
url = "https://api.github.com/repos/michealcannon/Iris-data-set-project"
filename = "rep.json"


response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

