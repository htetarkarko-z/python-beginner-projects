import string

def get_input():
    global message
    global shift_number

    message = input("Type your message: \n")
    shift_number = int(input("Type the shift number: \n"))
    message = list(message)


#declare global variables and check user input is correct
def main():
    global string_list
    global method
    global solution
    global encoded

    string_list = list(string.ascii_lowercase)
    encoded = []
    solution = ''
    method = input("Type 'encode' to encrypt, 'decode' to decrypt: \n")

    if method == 'encode':
        get_input()
        encode(message, shift_number)
    elif method == 'decode':
        get_input()
        decode(message, shift_number)
    else:
        print("Wrong input please try again.")
        main()


#search user input in stringlist and add shift num to that
def encode(message, shift_number):
    solution = ''
    for char in message:
        index = string_list.index(char)
        encoded = string_list[index + shift_number]
        solution += encoded
    print(f'Here is the encoded result: {solution}')


#shearch user input stringlist and remove shift num to that
def decode(message, shift_number):
    solution = ''
    for char in message:
        index = string_list.index(char)
        decoded = string_list[index - shift_number]
        solution += decoded
    print(f'Here is the decoded result: {solution}')


#calling the main function
main()