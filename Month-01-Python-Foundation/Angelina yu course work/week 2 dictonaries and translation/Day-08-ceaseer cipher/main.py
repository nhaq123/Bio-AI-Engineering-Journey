letters = "abcdefghijklmnopqrstuvwxyz"






def encrypt(msg, shift):
    encode_msg = ""
    for char in msg:  # Better to iterate directly over characters
        if char in letters:
            position = letters.index(char)
            new_position = position + shift
            encode_msg += letters[new_position]
        else:
            encode_msg += char  # Keep spaces and punctuation
    print(f"The encoded text is {encode_msg}")

def decrypt(msg,shift):
    decode_msg = ""
    for char in msg:
        if char in letters:
            position = letters.index(char)
            new_position = position - shift
            decode_msg += letters[new_position]
    print(f"The decoded text is {decode_msg}")
decide = True
while decide :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        msg = input("enter the message you want to encrypt")
        shift = int(input("enter the shift number"))
        encrypt(msg, shift)
    elif direction == "decode":
        msg = input("enter the message you want to decrypt")
        shift = int(input("enter the shift number"))
        decrypt(msg ,shift)
    
    
    else:
        print("You entered error message ")  
    result = input ("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        decide = False
        print("Good bye")

    

