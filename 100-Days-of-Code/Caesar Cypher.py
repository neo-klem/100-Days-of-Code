alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for i in original_text:
        z = alphabet.index(i) + shift_amount
        if z >= 26:
            x = z - 26
            encrypted_text += alphabet[x]
        else:
            encrypted_text += alphabet[alphabet.index(i) + shift_amount]
    print(encrypted_text)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = "zoran" # input("Type your message:\n").lower()
shift = 1 # int(input("Type the shift amount:\n"))

encrypt(text, shift)