from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def get_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice('+', '-', '*')
    
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    question = f'{num1} {operator} {num2}'

    return question, answer
