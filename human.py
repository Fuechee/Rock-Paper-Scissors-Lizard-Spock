from player import Player

class Human(Player):
    def __init__(self):
        super().__init__('Player')

    def gesture_selected(self):
        print("Select an gesture")
        print('Rock, Paper, Scissors, Lizard, Spock')
        self.gesture_selected = input('')
