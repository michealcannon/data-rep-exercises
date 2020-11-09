import requests, json
from xlwt import *

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"


response = requests.get(url)
data = response.json()
