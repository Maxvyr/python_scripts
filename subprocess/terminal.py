import os
import subprocess

# shell=True -> say it's a command not a program
# capture_output=True -> save result in variable
# universal_newlines=True -> return stdout in str
# os.getcwd() => show current folder
while True:
    user_input = input(f"{os.getcwd()} > ")
    if user_input == "exit":
        break

    list_param = user_input.split(" ")  # transform str in list split with space

    if len(list_param) == 2 and list_param[0] == "cd":
        # print(f"{list_param[0]} && {list_param[1]}")
        try:
            os.chdir(list_param[1])
        except FileNotFoundError:
            print(f"Folder {list_param[1]} doesn't exist, try a new one")
    else:
        res = subprocess.run(user_input, shell=True, capture_output=True, universal_newlines=True)

        print(res.stdout)
        print(res.stderr)  # return value if error
