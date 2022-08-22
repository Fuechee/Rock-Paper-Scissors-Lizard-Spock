from human import Human
from ai import AI
from time import sleep
import random

class Game:
    def __init__(self):
        self.player1 = Human('Player1')
        self.player2 = Human('Player2')
        self.player3 = AI()

    
    def run_game(self):
        self.display_welcome()
        self.play_game()

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

    def play_game(self):
        player1wins = 0
        player2wins = 0
        player3wins = 0
        while True:
            users_input = input('Single Player or Multiplayer: ')
            if users_input == 'Single Player':
                break
            elif users_input == 'Multiplayer':
                break
            else:
                print('Invaild response, please try again.')
        winner = False
        play_style1 = users_input
        if play_style1 == "Single Player":
            play_style1 = True
            while winner == False:
                self.player1.gesture_select()
                self.player3.gesture_select()
                if (self.player1.gesture_selected == 'Rock') and (self.player3.gesture_selected == 'Lizard' or 'Scissor'):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player3.gesture_selected == "Rock") and (self.player1.gesture_selected == "Lizard" or "Scissor"):
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player3wins += 1
                elif (self.player1.gesture_selected == "Paper") and (self.player3.gesture_selected == "Rock" or "Spock"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player3.gesture_selected == "Paper") and (self.player1.gesture_selected == "Rock" or "Spock"):
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player3wins += 1
                elif (self.player1.gesture_selected == "Scissors") and (self.player3.gesture_selected == "Paper" or "Lizard"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player3.gesture_selected == "Scissors") and (self.player1.gesture_selected == "Paper" or "Lizard"):
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player3wins += 1   
                elif (self.player1.gesture_selected == "Lizard") and (self.player3.gesture_selected == "Paper" or "Spock"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player3.gesture_selected == "Lizard") and (self.player1.gesture_selected == "Paper" or "Spock"):
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player3wins += 1
                elif (self.player1.gesture_selected == "Spock") and (self.player3.gesture_selected == "Rock" or "Scissors"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player3.gesture_selected == "Spock") and (self.player1.gesture_selected == "Rock" or "Scissors"):
                    print(f' {self.player3.name} chose {self.player3.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player3wins += 1
                elif (self.player1.gesture_selected) == (self.player3.gesture_selected):
                    print("Draw! Rematch!")
                    return    
                if  player1wins == 2:
                    print(f'{self.player1.name} WINS')
                    winner = True
                elif player3wins == 2:
                    print(f'{self.player3.name} WINS')
                    winner = True
        play_style2 = users_input
        if play_style2 == "Multiplayer":
            play_style2 = True
            while winner == False:
                self.player1.gesture_select()
                self.player2.gesture_select()
                if (self.player1.gesture_selected == "Rock") and (self.player2.gesture_selected == "Lizard" or "Scissor"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player2.gesture_selected == "Rock") and (self.player1.gesture_selected == "Lizard" or "Scissor"):
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player2wins += 1
                elif (self.player1.gesture_selected == "Paper") and (self.player2.gesture_selected == "Rock" or "Spock"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player2.gesture_selected == "Paper") and (self.player1.gesture_selected =="Rock" or "Spock"):
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player2wins += 1
                elif (self.player1.gesture_selected == "Scissors") and (self.player2.gesture_selected =="Paper" or "Lizard"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player2.gesture_selected == "Scissors") and (self.player1.gesture_selected =="Paper" or "Lizard"):
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    print('')
                    player2wins += 1    
                elif (self.player1.gesture_selected == "Lizard") and (self.player2.gesture_selected =="Paper" or "Spock"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player2.gesture_selected == "Lizard") and (self.player1.gesture_selected =="Paper" or "Spock"):
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player2wins += 1
                elif (self.player1.gesture_selected == "Spock") and (self.player2.gesture_selected =="Rock" or "Scissors"):
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print('')
                    player1wins += 1
                elif (self.player2.gesture_selected == "Spock") and (self.player1.gesture_selected =="Rock" or "Scissors"):
                    print(f' {self.player2.name} chose {self.player2.gesture_selected}')
                    print(f' {self.player1.name} chose {self.player1.gesture_selected}')
                    print('')
                    player2wins += 1
                elif (self.player1.gesture_selected) == (self.player2.gesture_selected):
                    print("Draw! Rematch!")
                    return         
                if  player1wins == 2:
                    print(f'{self.player1.name} WINS')
                    winner = True
                elif player2wins == 2:
                    print(f'{self.player2.name} WINS')
                    winner = True