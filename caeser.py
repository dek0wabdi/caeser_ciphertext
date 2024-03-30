def encrypt(text,shift):#definition of a function that takes 2 params.
    encrypted_text="" #initializes an empty string named encrypted_text where the encrypted text will be stored.
    for char in text: #This line starts a loop that iterates over each character in the input text.

        if char.isalpha (): #checks if the character is a letter.

            shifted =ord(char)+shift #This line calculates the ASCII value of the current character (ord(char)), adds the shift value to it, and assigns the result to the variable shifted.
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted +=26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted +=26
            encrypted_text+= chr(shifted)
        else:
            encrypted_text+=char
    return encrypted_text
def decrypt(text,shift):
    return encrypt(text,-shift)
def main():
    text=input("Enter the text you want to be encrypted: ")
    shift=int(input("Enter the shift value, must be positive: "))

    encrypted_text=encrypt(text,shift)
    print("The encrypted text is:",encrypted_text)

    decrypted_text=decrypt(encrypted_text,shift)
    print("The decrypted text is:",decrypted_text)

if __name__ == "__main__":
    main()
