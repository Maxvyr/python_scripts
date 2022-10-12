import requests
import json


res = requests.get("https://codeavecjonathan.com/res/programmation.txt")
if res.status_code == 200:
    res.encoding = "utf-8"
    print(res.text)
else:
    print(f"ERROR {res.status_code}")

res = requests.get("https://google.com/no_file.html")
if res.status_code == 200:
    res.encoding = "utf-8"
    print(res.text)
else:
    print(f"ERROR {res.status_code}")

res = requests.get("https://jsonplaceholder.typicode.com/photos")
if res.status_code == 200:
    res.encoding = "utf-8"
    photos = json.loads(res.text)
    print(f"Total = {len(photos)} Photos")
else:
    print(f"ERROR {res.status_code}")
