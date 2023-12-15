alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

new_alphabet = alphabet * 2


def encrypt(plain_text, shift_amount):
    encrypted_message = " "
    for letter in plain_text:
        if letter != " ":
            index_to_print = alphabet.index(letter) + shift_amount
            encrypted_message += new_alphabet[index_to_print]
        else:
            encrypted_message += " "
    print(f"Your encrypted message is: {encrypted_message}.")


def decrypt(plain_text, shift_amount):
    encrypted_message = " "
    for letter in plain_text:
        if letter != " ":
            index_to_print = alphabet.index(letter) - shift_amount
            encrypted_message += new_alphabet[index_to_print]
        else:
            encrypted_message += " "
    print(f"Your encrypted message is: {encrypted_message}.")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
