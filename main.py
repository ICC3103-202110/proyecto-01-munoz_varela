import random
import time
import os
from copy import copy
from board import Board
from player_1 import Player_1
from player_2 import Player_2
from player_3 import Player_3
from player_4 import Player_4
from influences import Influences

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    n_players = int(input( "How many players are playing today: ")) #Nunber of players #ELIMINAR POSIBILIDAD DE CRASH CON STRS
    while (n_players < 3) or (n_players > 4):
        n_players = int(input( "How many players are playing today: "))

    names = []
    a = ["\033[;34m","\033[1;34m"]
    b = ["\x1b[;33m","\033[1;33m"]
    c = ["\033[;31m","\033[1;31m"]
    d = ["\033[;32m","\033[1;32m"]
    index = [a,b,c,d]
    for i in range(0,n_players):
        print("\n")
        print(""+index[i][0]+"╔════════════════════════════════════════╗    ~This will be the max leight of")
        print("║                                        ▼     your name showed in the game. ")
        x = input("Tell me you name player "+str(i+1)+": "+"\033[1;37m") #Set the names
        x = x[0:15]
        names.append(x)
        cls()

    cards=["Duke","Duke","Duke","Murderer","Murderer","Murderer"
    "","Captain","Captain","Captain","Ambassador","Ambassador"
    "","Ambassador","Countess","Countess","Countess"]
    random.shuffle(cards) #Randomizer

    cards_player_1= [cards[0],cards[1]]
    cards_player_2= [cards[2],cards[3]]
    cards_player_3= [cards[4],cards[5]]

    player_1 = Player_1(names[0] ,cards_player_1, [False,False], 2, a )#Azul
    player_2 = Player_2(names[1] ,cards_player_2, [False,False], 2, b)#Amarillo
    player_3 = Player_3(names[2] ,cards_player_3, [False,False], 2, c)#Rojo
 
    if n_players == 4:
        cards_player_4 = [cards[6],cards[7]]
        player_4 = Player_4(names[3],cards_player_4, [False,False], 2, d)#Verde
        desk_cards = [cards[8],cards[9],cards[10],cards[11],cards[12],cards[13],cards[14]]
    else:
        player_4 = Player_4("Null","Null","Null",0, "Null")
        desk_cards = [cards[6],cards[7],cards[8],cards[9],cards[10],cards[11],cards[12],cards[13],cards[14]]

    ref = [player_1,player_2,player_3,player_4]  
    board = Board(n_players,desk_cards,0,"\033[1;37m")
    influences = Influences()
    
    board.welcome(player_1,player_2,player_3,player_4)
    while True:
        cls()
        turn = board.turn 
        board.waiter(ref[turn])
        board.evaluator(player_1,player_2,player_3,player_4)
        if board.n_players == 3:
            break
        influences.play(board,player_1,player_2,player_3,player_4)
        time.sleep(3)



if __name__ == "__main__":
    main()