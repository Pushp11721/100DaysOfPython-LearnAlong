#We can also create a file using it if it doesn't exist
with open("new_file.txt",mode="w") as file:
    file.write("New file created!")

#Remember this only works in write mode -> "w"