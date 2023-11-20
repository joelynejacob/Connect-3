from game import Player
from connect3 import Action

import random, math


class RandomPlayer(Player):
    def choose_action(self, state):
        legal_actions = state.actions(self.char)
        return random.choice(legal_actions)


class MinimaxPlayer(Player):
    def __init__(self, char):
        super().__init__(char)
        self.depth = 2
        if self.char == "X":
            self.opponent_char = "O"
        else:
            self.opponent_char = "X"

    def choose_action(self, state):
        action = self.minimaxDecider(state)
        return action

    def evaluate(self, state):
        winner = state.winner()
        if winner == self.char:
            return 1
        elif winner:
            return -1
        else:
            return 0

    def minimaxDecider(self, state):
        legal_actions = state.actions(self.char)
        max_val = -math.inf
        move = legal_actions[0]
        for legal_action in legal_actions:
            new_state = state.clone().execute(legal_action)
            val = self.minimax(new_state, False)
            if val>max_val:
                max_val = val
                move = legal_action
        return move
        
    def minimax(self, state, maximizing_player):
        if state.game_over():
            return self.evaluate(state)

        if maximizing_player:
            legal_actions = state.actions(self.char)
            max_value = -math.inf
            for max_action in legal_actions:
                max_new_state = state.clone().execute(max_action)
                value = self.minimax(max_new_state, False)
                max_value = max(value, max_value)

            return max_value*0.5
        else:
            opponent_actions = state.actions(self.opponent_char)
            opponent_value = math.inf
            for opponent_action in opponent_actions:
                opponent_new_state = state.clone().execute(opponent_action)
                value = self.minimax(opponent_new_state, True)
                opponent_value = min(value, opponent_value)
            return opponent_value*0.5
if __name__ == '__main__':
    from game import Game

    player1 = MinimaxPlayer('X')
    player2 = MinimaxPlayer('O')

    game = Game(player1, player2)
    game.play()