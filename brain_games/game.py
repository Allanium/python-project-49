from prompt import string

ROUND = 3


def game(some_game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(some_game.DESCRIPTION)
    for i in range(ROUND):
        question, answer = some_game.get_round()
        print(f'Question: {question}')
        user_answer = string('Your answer:  ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
