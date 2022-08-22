from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
 
    def gesture_select(self):
        print("Select an gesture")
        print('Rock, Paper, Scissors, Lizard, Spock')
        self.gesture_selected = input('Please enter a gesture: ')
