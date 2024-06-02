

def caesar_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
            else:
                result += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            result += char
    return result

# User input
text = input("Please enter your message here: ")
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)



