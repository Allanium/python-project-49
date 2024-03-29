from prompt import string

ROUND = 3


def run_game(some_game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(some_game.DESCRIPTION)
    
    for _ in range(ROUND):
        question, answer = some_game.get_round()
        print(f'Question: {question}')
        user_answer = string('Your answer:  ')
        
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {name}!")
        else:
            print('Correct!')
            return
    print(f'Congratulations, {name}!')
