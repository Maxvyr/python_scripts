import json

# serialize and deserialize


# WRITE
person = {
    "name": "Lenny",
    "age": 2,
    "amis": ["Yuna", "Judith", "Maêlle"]
}

person_json = json.dumps(person)

f = open("file.json", "w")
f.write(person_json)
f.close()

# READ
f = open("file.json", "r")
data = f.read()
person = json.loads(data)
print(person)
f.close()
print(person["name"])
