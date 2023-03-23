# username = super
# password = print()
def encode(password):
    encoded = str(password)
    for char in password:
        digit = int(char)
        encoded += str(digit + 3 % 10)
    return encoded


def decode(password):
    decoded = ''
    for char in password:
        digit = int(char)
        decoded += str(digit - 3 % 10)

    return decoded


while True:
    print("Menu\n-------------\n")
    print("1. Encode\n2. Decode\n3. Quit")
    print()
    yeah = int(input("Please enter an option: "))
    if yeah == 1:
        password = int(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!\n")
    if yolo == 2:
        encoded = encode(password)
        print(f'The encoded password is {encoded}, and the original password is {decode(str(password))}\n')
    if yeah == 3:
        break
