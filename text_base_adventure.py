def play():
    life_remaining = 3
    print("Write n, e, s, w for north, east, south, west")
    message = "Where do you wants to go. You are in "
    while life_remaining > 0:
        get_input = input(message + "common room: ").casefold()
        if get_input == 'n':
            get_input = input(message + "bear room: ")
            if get_input == 'e':
                get_input = input(message + "grave: ")
                if get_input == 's':
                    get_input = input(message + "tunnel: ")
                    if get_input == 'e':
                        print("You won the game !!!")
                        break
                else:
                    life_remaining -= 1
                    print(f"You hit the wall and left {life_remaining} life")
            else:
                life_remaining -= 1
                print(f"You hit the wall and left {life_remaining} life")
        elif get_input == 's':
            get_input = input(message + "monster room: ")
        else:
            life_remaining -= 1
            print(f"You hit the wall and left {life_remaining} life")
    else:
        print("You lost the game")


play()