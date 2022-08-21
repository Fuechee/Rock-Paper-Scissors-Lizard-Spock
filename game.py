from human import Human
from ai import AI
from time import sleep
import random

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.player3 = AI()
        self.gestures = ['Rock','Paper','Scissors','Lizard','Spock']
    
    def run_game(self):
        self.display_welcome()
        self.play_game()
        self.select_gesture()
        self.display_winner()


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
        player1 = ''
        player2 = ''
        player3 = ''
        player1wins = 0
        player2wins = 0
        player3wins = 0
        users_input = ''
        print("Single Player or Multiplayer")
        play_style1 =input(" ").upper
        while users_input is not 'Single Player' or 'Multiplayer':
                print('Invalid option. Try again')
        users_input = input('Single Player or Multiplayer')
        winner = False
        if play_style1 == "Single Player":
            play_style1 = True
            while winner==False:
                self.select_gesture(AI=True)
                if player1 =="Rock" and player3 =="Lizard" or "Scissor":
                    print(player1)
                    player1wins+1
                elif player3 =="Rock" and player1 =="Lizard" or "Scissor":
                    print(player3)
                    player3wins+1
                elif player1 =="Paper" and player3 =="Rock" or "Spock":
                    print(player1)
                    player1wins+1
                elif player3 =="Paper" and player1 =="Rock" or "Spock":
                    print(player3)
                    player3wins+1
                elif player1 =="Scissors" and player3 =="Paper" or "Lizard":
                    print(player1)
                    player1wins+1
                elif player3 =="Scissors" and player1 =="Paper" or "Lizard":
                    print(player3)
                    player3wins+1   
                elif player1 =="Lizard" and player3 =="Paper" or "Spock":
                    print(player1)
                    player1wins+1
                elif player3 =="Lizard" and player1 =="Paper" or "Spock":
                    print(player3)
                    player3wins+1
                elif player1 =="Spock" and player3 =="Rock" or "Scissors":
                    print(player1)
                    player1wins+1
                elif player3 =="Spock" and player1 =="Rock" or "Scissors":
                    print(player3)
                    player3wins+1
                elif player1 == player3:
                    print("Draw! Rematch!")
                    return 
                    
                if  player1wins == 2:
                    print(player1wins,"/",player3wins)
                    winner = True
                elif player3wins == 2:
                    print(player1wins,"/",player3wins)
                    winner = True
            