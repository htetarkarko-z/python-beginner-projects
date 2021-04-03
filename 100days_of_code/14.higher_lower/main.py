#import game data and art
from data import *
from art import *
#import random module
import random


#retrun a random dictionary from list
def generate_dict(data):
    choice = random.choice(data)
    return choice

#assign choices to the dict
choice_a = generate_dict(data)
choice_b = generate_dict(data)


#print message to the screen
def msg(choice):
    print(f"{choice['name']}, {choice['description']}, {choice['country']}")


#compare the two dict
def compare(choice_a, choice_b):
    count = 0
    while True:
        if count != 0:
            print(f'You\'re right! Current score: {count}')

        f"{msg(choice_a)}"
        print(vs)
        f"{msg(choice_b)}"

        user_choice = input("Who has the more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a' and choice_a['follower_count'] > choice_b['follower_count']:
            count += 1
        elif user_choice == 'b' and choice_b['follower_count'] > choice_a['follower_count']:
            count += 1
            choice_a = choice_b
        else:
            print(f"Sorry that was wrong. Final score {count}")
            break
        choice_b = generate_dict(data)

print(logo)
compare(choice_a, choice_b)