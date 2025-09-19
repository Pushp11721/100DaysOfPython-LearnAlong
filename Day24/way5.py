#Using relative file path - it is relative to where your current directory is
#path of way5 -        "D:/Coding/Python/Day24/way5.py"
#path of my_file.txt - "D:/Coding/my_file.txt"
#same                 
with open("../../my_file.txt") as file:
    content=file.read()
    print(content)
    print("way 5")