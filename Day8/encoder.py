alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']


#Task-1: Create a function called 'encrypt' that takes original_text and shift as an input and give encrypted_text in return
def encrypt(original_text,shift):
    encrypted_text=""
    for i in original_text:
        if i==" ":
            continue
        elif i in alphabet:
            if alphabet.index(i)+shift+1>len(alphabet):
                new_shift=(alphabet.index(i)+shift)-len(alphabet)
                encrypted_text+=alphabet[new_shift]
            else:
                encrypted_text+=alphabet[alphabet.index(i)+shift]
    return encrypted_text

#Task-1: Create a function called 'decrypt' that takes original_text and shift as an input and give decrypted_text in return
def decrypt(original_text,shift):
    decrypted_text=""
    for i in original_text:
        if i==" ":
            continue
        elif i in alphabet:
                decrypted_text+=alphabet[alphabet.index(i)-shift]
    return decrypted_text

#Now create if-else loop for user based direction
user_need=True
while user_need:
    # take inputs required
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n"))
    if direction=="encode":
        print(encrypt(text,shift))
    else:
        print(decrypt(text,shift))
    ask=input("Do you want to continue? type 'Yes' or 'No'\n").lower()
    if ask=="no":
        user_need=False

