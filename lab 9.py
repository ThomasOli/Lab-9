def main():
    quit = False
    while quit != True:
        print()
        menu()
        print()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = int(input('Please enter your password to encode: '))
            encoded_password = encode(password)
        elif option == 2:
            decode(encoded_password)
        elif option == 3:
            quit = True
            return

def encode(password):
    encode_list = []
    password_str = str(password)
    for i in password_str:
        encode_list.append(int(i) + 3)
    print('Your password has been encoded and stored!')
    return encode_list

def decode(encoded_password):
    decode_list = []
    decode_list_str = []
    encoded_password_join = []
    for i in encoded_password:
        decode_list.append(int(i) - 3)
    # minuses 3 from the encoded password
    for i in decode_list:
        decode_list_str.append(str(i))
    # joins the list together
    for i in encoded_password:
        encoded_password_join.append(str(i))
    # makes the encoded password a string to later join it
    encoded_password_join = (''.join(encoded_password_join))
    decoded_password = (''.join(decode_list_str))
    return print(f'The encoded password is {encoded_password_join}, and the original password is {decoded_password}.')

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

if __name__ == "__main__":
    main()