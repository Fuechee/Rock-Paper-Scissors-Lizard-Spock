from player import Player
import random 
class AI(Player):
    def __init__(self, name):
        super().__init__(name)

    def gesture_selected(self):
        self.gesture_selected = random.choice(self.gestures)
