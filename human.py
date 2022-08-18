from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def gesture_selected(self):
        print("Select an gesture")
        print('Rock, Paper, Scissors, Lizard, Spock')
        self.gesture_selected = input('')
        while users_input is not self.gestures:
            print('Invalid option. Try again')
            users_input = input('Please enter a gesture: ')
        self.gesture_selected = users_input
