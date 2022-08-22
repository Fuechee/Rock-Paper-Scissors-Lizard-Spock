from player import Player
import random 

class AI(Player):
    def __init__(self):
        super().__init__("AI")

    def gesture_select(self):
        self.gesture_selected = random.choice(self.gestures)
