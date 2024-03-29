from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_round():
    start_progression = randint(1, 100)
    step = randint(2, 5)
    number_of_digits = randint(5, 10)
    end_progression = start_progression + step * number_of_digits
    progression = list(range(start_progression, end_progression, step))
    random_number = randint(0, number_of_digits - 1)
    answer = str(progression[random_number])
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question += str(number) + ' '
    question = str(question.strip())
    return question, answer
