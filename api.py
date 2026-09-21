import requests

data = requests.get("https://official-joke-api.appspot.com/random_joke")
print(data.json())