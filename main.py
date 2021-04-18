import random
from board import Board
from player_1 import Player_1
from player_2 import Player_2
from player_3 import Player_3
from player_4 import Player_4

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
    if n_players == 4:
        cards_player_4 = [cards[6],cards[7]]

    player_1 = Player_1(names[0] ,cards_player_1, [False,False], 2)
    player_2 = Player_2(names[1] ,cards_player_2, [True,False], 2)
    player_3 = Player_3(names[2] ,cards_player_3, [True,True], 2)
    if n_players == 4:
        player_4 = Player_4(names[3],cards_player_4, [False,True], 2)
    else:
        player_4 = Player_4(0,0,0,0)
        
    board = Board(n_players,0,1)
    print("\n")
    board.showboard(player_1,player_2,player_3,player_4)
    print("\n")
    board.evaluator(player_1,player_2,player_3,player_4)
    print("\n")
    board.showboard(player_1,player_2,player_3,player_4)
    print("\n")

    print(player_1.vcards)
if __name__ == "__main__":
    main()