import random
from copy import copy
from board import Board
from player_1 import Player_1
from player_2 import Player_2
from player_3 import Player_3
from player_4 import Player_4
from influences import Influences

def main():
    n_players = int(input( "How many players are playing today:")) #Nunber of players #ELIMINAR POSIBILIDAD DE CRASH CON STRS
    while (n_players < 3) or (n_players > 4):
        n_players = int(input( "How many players are playing today:"))

    names = []
    for i in range(1,n_players+1):
        x = input("Tell me you name player "+str(i)+": ") #Set the names
        names.append(x)

    cards=["Duke","Duke","Duke","Murderer","Murderer","Murderer"
    "","Captain","Captain","Captain","Ambassador","Ambassador"
    "","Ambassador","Countess","Countess","Countess"]
    random.shuffle(cards) #Randomizer

    cards_player_1= [cards[0],cards[1]]
    cards_player_2= [cards[2],cards[3]]
    cards_player_3= [cards[4],cards[5]]

    player_1 = Player_1(names[0] ,cards_player_1, [False,False], 2)
    player_2 = Player_2(names[1] ,cards_player_2, [True,True], 2)
    player_3 = Player_3(names[2] ,cards_player_3, [True,False], 2)

    if n_players == 4:
        cards_player_4 = [cards[6],cards[7]]
        player_4 = Player_4(names[3],cards_player_4, [False,True], 2)
        desk_cards = [cards[8],cards[9],cards[10],cards[11],cards[12],cards[13],cards[14]]
    else:
        player_4 = Player_4(0,0,0,0)
        desk_cards = [cards[6],cards[7],cards[8],cards[9],cards[10],cards[11],cards[12],cards[13],cards[14]]
        
    board = Board(n_players,desk_cards,1)
    influences = Influences()

    print("Las monedas del Jugador 1 son: "+str(player_1.coins))
    influences.play(board,player_1,player_2,player_3,player_4)
    print("Ahora.. las monedas del Jugador 1 son: "+str(player_1.coins))
    """
    print("\n")
    board.showboard(player_1,player_2,player_3,player_4)
    print("\n")
    board.evaluator(player_1,player_2,player_3,player_4)
    print("\n")
    board.showboard(player_1,player_2,player_3,player_4)
    print("\n")
    """

if __name__ == "__main__":
    main()