# human.py
from game import Player
from connect3 import Action

class HumanPlayer(Player):
    def choose_action(self, state):
        legal_actions = state.actions(self.char)
        for i, action in enumerate(legal_actions):
            print(f"{i}: {action}")
        column = int(input(f"Please choose an action: "))
        return Action(self.char, column)

if __name__ == '__main__':
    from game import Game

    player1 = HumanPlayer('X')
    player2 = HumanPlayer('O')

    game = Game(player1, player2)
    game.play()
