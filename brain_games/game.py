from prompt import string

ROUNDS = 3

def game(some_game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print({logic.DESCRIPTION})
    for i in range(ROUNDS):
        question, answer = logic.get_round()
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
