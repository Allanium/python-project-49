from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def get_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = ['+', '-', '*']
    random_operator = choice(operator)

    if random_operator == '+':
        answer = num1 + num2
    elif random_operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f'{num1} {random_operator} {num2}'

    return question, answer
