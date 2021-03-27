import random

#generate random word
word_list = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
chosen_word = random.choice(word_list)
list_of_string = []
life = 6

for i in range(len(chosen_word)):
    list_of_string.append('_')
print(chosen_word)


while '_' in list_of_string:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if guess == char:
            list_of_string[position] = guess

    if guess not in list_of_string:
        life -= 1
        print(f'You lost a life, {life} life remain')
        if life == 0:
            print("You lost the game")
            break
    print(list_of_string)
print("You won")