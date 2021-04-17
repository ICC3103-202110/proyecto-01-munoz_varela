import random

class Player_1:

    def __init__(self, names, cards, coins):
        self.names = names
        self.cards = cards
        self.coins = 2


class Player_2:

    def __init__(self, names, cards, coins):
        self.names = names
        self.cards = cards
        self.coins = 2


class Player_3:

    def __init__(self, names, cards, coins):
        self.names = names
        self.cards = cards
        self.coins = 2


class Player_4:

    def __init__(self, names, cards, coins):
        self.names = names
        self.cards = cards
        self.coins = 2



def main():
    n_players = int(input( "How many players are playing today:")) #Nunber of players #ELIMINAR POSIBILIDAD DE CRASH CON STRS
    while (n_players < 3) or (n_players > 4):
        n_players = int(input( "How many players are playing today:"))

    names = []
    for i in range(1,n_players+1):
        x = input("Tell me you name player "+str(i)+": ")
        names.append(x)

    cards=["duke","duke","duke","murderer","murderer","murderer"
    "","captain","captain","captain","ambassador","ambassador","ambassador","countess","countess","countess"]
    random.shuffle(cards) #Randomizer

    cards_player_1= [cards[0],cards[1]]
    cards_player_2= [cards[2],cards[3]]
    cards_player_3= [cards[4],cards[5]]
    if n_players == 4:
        cards_player_4 = [cards[6],cards[7]]


    player_1 = Player_1(names[0],cards_player_1,True)
    player_2 = Player_2(names[1],cards_player_2,True)
    player_3 = Player_3(names[2],cards_player_3,True)
    if n_players == 4:
        player_4 = Player_4(names[3],cards_player_4,True)

    print("\n")
    print(player_1.names)
    print(player_1.cards)
    print(player_1.coins)

if __name__ == "__main__":
    main()