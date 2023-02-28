import random

list = ["KR", "CN", "TH", ""]
print("Let's go")

length = len(list) - 1
randNum = random.randint(0, length)

random.shuffle(list)


print("SO ====> " + list[randNum])
