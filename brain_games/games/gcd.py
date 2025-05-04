from random import randint


def gcd(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    
    return question, str(correct_answer)