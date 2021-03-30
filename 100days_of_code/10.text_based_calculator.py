def user_input():
    global first_num
    global second_num
    global operator
    global operator_list

    operator_list = ['+', '-', '*', '/']
    first_num = int(input("What is your first number?: "))
    operator = input(" + \n - \n * \n / \nPick an operation: ")
    second_num = int(input("What is your second number?: "))


def loop():
    global first_num
    global second_num
    global operator

    condition = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculator, or type '0' to exit: ".format(solution))
    if condition == 'y':
        first_num = solution
        operator = input(" + \n - \n * \n / \nPick an operation: ")
        second_num = int(input("What is your second number?: "))
        calculator(first_num, second_num, operator)
    elif condition == 'n':
        user_input()
        calculator(first_num, second_num, operator)


def calculator(first_num, second_num, operator):
    global solution
    solution = 0
    while operator not in operator_list:
        return operator
    if operator == '+':
        solution = first_num + second_num
    elif operator == '-':
        solution = first_num - second_num
    elif operator == '*':
        solution = first_num * second_num
    elif operator == '/':
        solution = first_num / second_num
    print(f'{first_num} {operator} {second_num} = {solution}')
    loop()


user_input()
calculator(first_num, second_num, operator)