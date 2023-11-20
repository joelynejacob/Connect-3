import random
from connect3 import State, Action
import util

class Player:
    def __init__(self, char):
        self.char = char

class Game:
    def __init__(self, player1, player2):
        self.players = {'X': player1, 'O': player2}
        self.state = State()

    def play(self):
        states_visited = [self.state.clone()]
        current_player = self.players['X']
        
        while not self.state.game_over():
            action = current_player.choose_action(self.state)
            self.state = self.state.execute(action)
            states_visited.append(self.state.clone())

            print(self.state.pprint_string())
            current_player = self.players['O'] if current_player == self.players['X'] else self.players['X']

        winner = self.state.winner()
        return winner, states_visited
