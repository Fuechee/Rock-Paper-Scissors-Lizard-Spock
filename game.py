from human import Human
from ai import AI
from time import sleep


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.player3 = AI()
        self.gestures = ['Rock','Paper','Scissors','Lizard','Spock']
    
    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print('Welcome to the game of Rock Paper Scissors Lizard Spock')
        sleep(0.5)
        print('Here are the instructions')
        sleep(0.5)
        print('Rock crushes Scissors')
        sleep(0.5)
        print('Scissors cuts Paper')
        sleep(0.5)
        print('Rock crushes Lizard')
        sleep(0.5)
        print('Lizard poisons Spock')
        sleep(0.5)
        print('Spock smashes Scissors')
        sleep(0.5)
        print('Sscissors decapitates Lizard')
        sleep(0.5)
        print('Lizard eats Paper')
        sleep(0.5)
        print('Paper disproves Spock')
        sleep(0.5)
        print('Spock vaporizes Rock')
        sleep(0.5)
        print('Winner will be best of 3')
        sleep(0.5)

    