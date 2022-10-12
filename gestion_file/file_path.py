import os.path

filename = os.path.join("rep", "sample.txt")

if os.path.exists(filename):
    print(f"file exist path : {filename}")
    f = open(filename, "r")
    txt = f.read()
    print(txt)
    f.close()
else:
    print("File doesn't exist")

# create  folder
# os.mkdir("rep")

# remove folder
# os.rmdir("rep")

# remove fil
# os.remove(filename)
