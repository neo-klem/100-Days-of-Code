alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z']

def caesar(direction, original_text, shift_amount):
    while True:
        if direction == "encode":
            encrypted_text = ""
            for i in original_text:
                z = alphabet.index(i) + shift_amount
                if z >= 26:
                    x = z - 26
                    encrypted_text += alphabet[x]
                else:
                    encrypted_text += alphabet[z]
            print(f"{encrypted_text}")
        elif direction == "decode":
            decrypted_text = ""
            for i in original_text:
                z = alphabet.index(i) - shift_amount
                decrypted_text += alphabet[z]
            print(decrypted_text)        

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = "mxcbkoqfq" # input("Type your message:\n").lower()
shift = 2 # int(input("Type the shift amount:\n"))

caesar(direction, text, shift)