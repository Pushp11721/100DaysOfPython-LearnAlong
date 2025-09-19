#Opening our file in append mode so that it will not clear all
#text that was present in the file at that time
with open("my_file.txt",mode="a") as file:
    file.write("\nHello, Golu here!")#this line will be added in text file
