import random
import time
from os import system, name
from copy import copy
from board import Board
from player_1 import Player_1
from player_2 import Player_2
from player_3 import Player_3
from player_4 import Player_4
from influences import Influences

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    clear()
    #Nunber of players #ELIMINAR POSIBILIDAD DE CRASH CON STRS
    n_players = int(input( "How many players are playing today: ")) 
    while (n_players < 3) or (n_players > 4):
        n_players = int(input( "How many players are playing today: "))

    names = []
    a = ["\033[0;34m","\033[1;34m","\033[6;30m"]
    b = ["\x1b[0;33m","\033[1;33m","\x1b[6;30m"]
    c = ["\033[0;31m","\033[1;31m","\033[6;30m"]
    d = ["\033[0;32m","\033[1;32m","\033[6;30m"]
    index = [a,b,c,d]
    for i in range(0,n_players):
        clear()
        print("\n")
        print(""+index[i][0]+"╔════════════════════════════════════════╗    ~"
        "This will be the max leight of")
        print("║                                        ▼     your name showed"
        " in the game. ")
        x = input("Tell me you name player "+str(i+1)+": "+"\033[1;37m")  
        #Set the names
        x = x[0:15]
        names.append(x)

    cards=["DUKE","DUKE","DUKE","MURDERER","MURDERER","MURDERER"
    "","CAPTAIN","CAPTAIN","CAPTAIN","AMBASSADOR","AMBASSADOR"
    "","AMBASSADOR","COUNTESS","COUNTESS","COUNTESS"]
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
        desk_cards = [cards[8],cards[9],cards[10],cards[11],cards[12],
        cards[13],cards[14]]
    else:
        player_4 = Player_4("Null","Null","Null",0, "Null")
        desk_cards = [cards[6],cards[7],cards[8],cards[9],cards[10],
        cards[11],cards[12],cards[13],cards[14]]

    ref = [player_1,player_2,player_3,player_4]  
    board = Board(n_players,desk_cards,0,"\033[1;37m")
    influences = Influences()
    
    #board.welcome(player_1,player_2,player_3,player_4)
    turn = 0
    n = board.n_players
    while True:
        clear()
        #board.waiter(ref[turn]) #Fix index for board.players_n
        board.evaluator(player_1,player_2,player_3,player_4)
        if n == 1:
            break
        influences.play(board,player_1,player_2,player_3,player_4)
        time.sleep(2)
        turn = board.turn 
        n = board.n_players
        if n == 4 and turn == 4:
            turn = 0
        elif n == 3 and turn ==3:
            turn = 0
        elif n == 2 and turn == 2:
            turn = 0

if __name__ == "__main__":
    main()