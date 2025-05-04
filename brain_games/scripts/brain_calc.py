from brain_games.engine import run_game
from random import choice, randint
from operator import add, mul, sub


def get_description():
    return 'What is the result of the expression?'


def generate_round():
    
    operations = {
        '+': add,
        '-': sub,
        '*': mul
    }
    
    operator = choice(list(operations.keys()))
    num1 = randint(1, 100) if operator != '*' else randint(2, 10)
    num2 = randint(1, 100) if operator != '*' else randint(2, 10)
    question = f'{num1} {operator} {num2}'
    correct_answer = operations[operator](num1, num2)

    return question, str(correct_answer)

def main():
    run_game(get_description(), generate_round)