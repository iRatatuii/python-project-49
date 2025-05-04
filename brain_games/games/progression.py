from random import randint


def get_progression():
    start_number = randint(1, 100)
    step = randint(1, 10)
    finish_number = start_number + step * 10
    progression = [num for num in range(start_number, finish_number, step)]
    return progression


def hide_one_number_in_progression(progression):
    hide_index = randint(0, 9)
    new_progression = progression[:]
    answer = new_progression[hide_index]
    new_progression[hide_index] = '..'
    return ' '.join(str(i) for i in new_progression), answer


def get_description():
    return 'What number is missing in the progression?'


def generate_round():
    question, answer = hide_one_number_in_progression(get_progression())
    return question, str(answer)
