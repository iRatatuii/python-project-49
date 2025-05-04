from prompt import string

from brain_games import cli
from brain_games.scripts.brain_games import greeting


def run_game(game_description, generate_round):
    user_name = cli.welcome_user()
    greeting()
    game_rules = game_description
    print(game_rules)
    rounds_to_win = 3
    
    for _ in range(rounds_to_win):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            result = (
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.!"
                      )
            print(result)
            print(f"Let's try again, {user_name}!")
            return
    else:
        print(f'Congratulations, {user_name}!')
