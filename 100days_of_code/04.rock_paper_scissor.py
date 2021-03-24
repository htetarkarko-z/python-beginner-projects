import random

#graphic
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#return graphic in a list
get_image = [rock, paper, scissors]
#get input from user
user = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n")
#check if the user input is a valid intenger
try:
    user = int(user)
except:
    print("Input Error only except int.")
#if user input is a range return an image of user choice
if user not in [0, 1, 2]:
    print('Invalid input. Try again')
else:
    print("Your choice is: ")
    print(get_image[user])
#randomazie computer
computer = random.randint(0, 2)
print("Computer choice is: ")
print(get_image[computer])

#main game conditional is in here
#r>s, s>p, p>r
if user == computer:
    print("It's a tie")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You won")
else:
    print("You lose")