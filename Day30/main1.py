#FileNotFoundError
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # value = a_dictionary["non_existent_key"]
except FileNotFoundError:
    # We specified what error it needs to detect, So now it move forward to next line and caught KeyError
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    #Now we will tackle KeyError
    #We can capture original error message by doing this
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")