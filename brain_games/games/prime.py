from random import randint


def is_prime(number):
    if number <= 1:
        return 'no'
    
    sqrt_number = int(number ** 0.5)
    for num in range(2, sqrt_number + 1):
        if number % num == 0:
            return 'no'
    return 'yes'
    
    
def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(1, 100)
    question = random_number
    correct_answer = is_prime(random_number)
    return str(question), correct_answer
