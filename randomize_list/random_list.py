import random

list = ["KR", "CN", "TH", ""]
print("Let's Begin")
length = len(list) - 1
list_2 = []
list_3 = []

random.shuffle(list)
list_2.append(list[length])
random.shuffle(list)
list_2.append(list[length])
random.shuffle(list)
list_2.append(list[length])
random.shuffle(list)
list_2.append(list[length])
random.shuffle(list)

print("Let's Begin 2")
length_2 = len(list_2) - 1

random.shuffle(list_2)
list_3.append(list_2[length_2])
random.shuffle(list_2)
list_3.append(list_2[length_2])
random.shuffle(list_2)
list_3.append(list_2[length_2])
random.shuffle(list_2)
list_3.append(list_2[length_2])
random.shuffle(list_2)

print("Let's Begin 3")
random.shuffle(list_3)
list_4 = list_3 + list_2
length_3 = len(list_3) - 1
print("Let's Begin 4")
random.shuffle(list_4)


print("SO ====> " + list_4[length_3])
