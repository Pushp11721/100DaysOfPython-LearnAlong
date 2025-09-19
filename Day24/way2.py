#using "with" keyword we don't need to close it manually
with open("my_file.txt",mode="w") as file:
    # content=file.read()
    file.write("New text.")#to do this we have to change the mode to "w"
    # print(content)
    print("way2")