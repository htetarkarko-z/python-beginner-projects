import random

#declare a list of words to play and assign them randomly
def main():
    global word
    global guessed_word
    global display
    global count
    global play_game
    global limit
    word_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(word_to_guess)
    guessed_word = []
    display = '_' * len(word)
    count = 0
    play_game = ''
    limit = 5

#popout to user and ask whether to wants to play or not
#if user input was invalid ask again
def play_loop():
    global play_game
    play_game = input('Do you want to play ?\n(y/n): ').casefold()
    while play_game not in ['y', 'n']:
        print('Invalid input')
        play_game = input('Do you want to play ?\n(y/n): ').casefold()
    if play_game == 'y':
        return main()
    elif play_game == 'n':
        return exit()

#main function to play with
def hangman():
    global display
    global guess
    global guessed_word
    global word
    global count
    #get user input
    guess = input(f'This is hangman:\n {display}\n enter your input: ').strip()
    #check if the user input is valid and is in correct to gueess if so replace guessed word with _ and display correctly
    #guessed word with display and limit the amount to play
    if len(guess) == 0 or len(guess) > 1 or guess.isnumeric():
        print ("invalid input")
        hangman()
    elif guess in word:
        guessed_word.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    elif guess in guessed_word:
        print('Try another letter')
    else:
        count += 1
        if count < 5:
            print(f'sorry wrong anwser {limit - count} remain')
        else:
            print(f'You lost the game.the anwser was: \n{guessed_word}{word}')
            play_loop

    #check user won or lose if not call func to play again
    if word == '_' * len(word):
        print('You won')
    elif count != limit:
        hangman()


main()
hangman()