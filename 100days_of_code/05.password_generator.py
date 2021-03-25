import random
import string

password_list = []

#get user input
print("Welcome to the Pypassword Generator")
letter_get = int(input("How many letter would you like in your password? \n"))
special_get = int(input("How many speical character would you like in you password? \n"))
number_get = int(input("How many number would you like in your password? \n"))

for i in range(1, letter_get + 1):
    password_list += random.choice(string.ascii_letters)
for i in range (1, special_get + 1):
    password_list += random.choice(string.punctuation)
for i in range (1, number_get + 1):
    password_list += random.choice(string.digits)
#shuffle the password list
random.shuffle(password_list)

#unpack the password list
password = ''
for char in password_list:
    password += char

print(password)