class Player:
    def __init__(self,name):
        self.name = name
        self.wins=int(0)
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.gesture_selected = " "