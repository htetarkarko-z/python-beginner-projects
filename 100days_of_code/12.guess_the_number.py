import random

logo = """
   _____   _    _   ______    _____    _____ 
  / ____| | |  | | |  ____|  / ____|  / ____|
 | |  __  | |  | | | |__    | (___   | (___  
 | | |_ | | |  | | |  __|    \___ \   \___ \ 
 | |__| | | |__| | | |____   ____) |  ____) |
  \_____|  \____/  |______| |_____/  |_____/ 

"""

number = random.randint(0, 100)
#for debug
print (number)

life = 0

def easy():
    return life + 10


def hard():
    return life + 5


def play():
    global life
    while life != 0:
        print(f'You have {life} attempts remaining to guess the number.')
        prompt = int(input("Make a guess: "))
        if prompt > number:
            print("Too high.\nGuess again")
            life -= 1
        elif prompt < number:
            print("Too low.\nGuess again")
            life -= 1
        elif prompt == number:
            print("Correct")
            print(f"The anwser is {number}")
            break

print(logo)
print("Welcome to the number guessing game.\n I'm thinking of a number between 1 and 100.")
start = ''
while start not in ['easy', 'hard']:
    start = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
if start == 'easy':
    life = easy()
    play()
elif start == 'hard':
    life = hard()
    play()