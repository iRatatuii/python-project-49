from random import randint

from prompt import string

from brain_games import cli
from brain_games.scripts.brain_games import greeting


def main():
    user_name = cli.welcome_user()
    greeting()
    game_rules = ('Answer "yes" if the number is even, '
                  'otherwise answer "no".')
    print(game_rules)
    flag = True
    count_games = 0
    
    while count_games < 3 and flag:
        random_number = randint(2, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count_games += 1
            if count_games == 3:
                print(f'Congratulations, {user_name}!')
        else:
            result = (
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.!"
                      )
            print(result)
            print(f"Let's try again, {user_name}!")
            flag = False
    
    
if __name__ == '__main__':
    
    main()