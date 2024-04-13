def encode(password):
    encoded_password = ""
    for char in password:
        if char in ["7", "8", "9"]:
            encoded_char = str(int(char) + 3)[1]
            encoded_password += encoded_char
        else:
            encoded_char = int(char) + 3
            encoded_password += str(encoded_char)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        if char in ["0", "1", "2"]:
            decoded_char = str(int(char) - 3 + 10)[-1]
            decoded_password += decoded_char
        else:
            decoded_char = int(char) - 3
            decoded_password += str(decoded_char)
    return decoded_password


def print_menu():
    print("""\nMenu
-------------
1. Encode
2. Decode
3. Quit\n""")


def main():
    encoded_password = None
    while True:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 3:
            return False


if __name__ == "__main__":
    main()
