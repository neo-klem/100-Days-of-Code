from caesarart import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z']

def caesar(direction, original_text, shift_amount):

    if direction == "encode":
        changed_text = ""
        for i in original_text:
            if i not in alphabet:
                changed_text += i
            else:    
                z = alphabet.index(i) + shift_amount
                if z >= 26:
                    x = z - 26
                    changed_text += alphabet[x]
                else:
                    changed_text += alphabet[z]
    else:
        changed_text = ""
        for i in original_text:
            if i not in alphabet:
                changed_text += i
            else:
                z = alphabet.index(i) - shift_amount
                changed_text += alphabet[z]
    print(f"Here's the {direction}d result: {changed_text}")        

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift amount:\n"))

caesar(direction, text, shift)