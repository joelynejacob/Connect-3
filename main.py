from game import Game
from human import HumanPlayer
from agent import RandomPlayer, MinimaxPlayer
import sys, util

if __name__ == '__main__':
    player1_type = sys.argv[1]
    player2_type = sys.argv[2]

    player1 = None
    player2 = None

    if player1_type == 'human':
        player1 = HumanPlayer('X')
    elif player1_type == 'random':
        player1 = RandomPlayer('X')
    elif player1_type == 'minimax':
        player1 = MinimaxPlayer('X')

    if player2_type == 'human':
        player2 = HumanPlayer('O')
    elif player2_type == 'random':
        player2 = RandomPlayer('O')
    elif player2_type == 'minimax':
        player2 = MinimaxPlayer('O')

    game = Game(player1, player2)
    winner, states_visited = game.play()

    print(f"{winner} wins")
    util.pprint(states_visited)
