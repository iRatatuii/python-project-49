from random import randint

from brain_games.engine import run_game


def get_description():
    return ('Answer "yes" if the number is even, '
            'otherwise answer "no".')


def generate_round():
    random_number = randint(2, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return str(random_number), correct_answer


def main():
    run_game(get_description(), generate_round)