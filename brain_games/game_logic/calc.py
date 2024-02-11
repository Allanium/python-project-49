from random import choise, randint

DESCRIPTION = 'What is the result of the expression?'

def get_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    random_key = choice(list(answers.keys()))
    answer = str(answers[random_key])
    question = f'{num_1} {random_key} {num_2}'

    return question, answer
