from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d <= n / 2:
        if n % d == 0:
            return False
        d += 1
    return True


def get_round():
    number = randint(2, 101)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
