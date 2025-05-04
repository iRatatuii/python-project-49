from brain_games.engine import run_game
from brain_games.games.even import get_description, generate_round

def main():
    
    run_game(get_description(), generate_round)