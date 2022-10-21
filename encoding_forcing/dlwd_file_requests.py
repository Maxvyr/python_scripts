import requests

res = requests.get("https://konachan.com/sample/679d359386dc110303c371ca82a8bec5/Konachan.com/sample.jpg")

if res.status_code == 200:
    print("Start Write file")
    f = open("waifu.jpg", "wb")
    f.write(res.content)
    f.close()
    print("Finish write file")
else:
    print(f"ERROR {res.status_code}")
