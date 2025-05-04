from brain_games.engine import run_game
from brain_games.games.prime import generate_round, get_description


def main():
    run_game(get_description(), generate_round)