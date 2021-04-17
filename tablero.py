import random
n_players=int(input( "How many players are playing today") )
while n_players <3 or n_players >4:
    n_players=int(input( "How many players are playing today"))

cards=["duke","duke","duke","murderer","murderer","murderer","captain","captain","captain","ambassador","ambassador","ambassador","countess","countess","countess"]
random.shuffle(cards)
cards_player_1= []
cards_player_2= []
cards_player_3= []
cards_player_4=[]
decks_cards=[]
def give_cards (x):
    if n_players==3:
        cards_player_1.append(cards[0])
        cards_player_1.append(cards[1])
        cards_player_2.append(cards[2])
        cards_player_2.append(cards[3])
        cards_player_3.append(cards[4])
        cards_player_3.append(cards[5])
        decks_cards.append(cards[5])
        decks_cards.append(cards[6])
        decks_cards.append(cards[7])
        decks_cards.append(cards[8])
        decks_cards.append(cards[9])
        decks_cards.append(cards[10])
        decks_cards.append(cards[11])
        decks_cards.append(cards[12])
        decks_cards.append(cards[13])
        decks_cards.append(cards[14])
    else: 
        cards_player_1.append(cards[0])
        cards_player_1.append(cards[1])
        cards_player_2.append(cards[2])
        cards_player_2.append(cards[3])
        cards_player_3.append(cards[4])
        cards_player_3.append(cards[5])
        cards_player_4.append(cards[6])
        cards_player_4.append(cards[7])
        decks_cards.append(cards[7])
        decks_cards.append(cards[8])
        decks_cards.append(cards[9])
        decks_cards.append(cards[10])
        decks_cards.append(cards[11])
        decks_cards.append(cards[12])
        decks_cards.append(cards[13])
        decks_cards.append(cards[14])
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
    hiden_cards=["*","*"]
    print("\n")
    print(player_1.names ,"you have" ,player_1.coins, "coins")
    print(player_1.names)
    print(player_1.cards)
    print(hiden_cards)
    print(hiden_cards)
    print(hiden_cards)
    print(hiden_cards)
    print(player_2.names, "it´s your time to play")
    a=input(" to see your cadrs please enter yes:")
    while a!= "yes":
        print(player_2.names, "please enter yes to continue with the game")
        a=input( "to see your cadrs please enter yes:")
    print(player_2.names, "you have" ,player_2.coins, "coins")
    print(hiden_cards)
    print(player_2.cards)
    print(hiden_cards)
    print(hiden_cards)
    print(hiden_cards)
    print(player_3.names, "it´s your time to play")
    a=input( "to see your cadrs please enter yes:")
    while a!= "yes":
        print(player_3.names, "please enter yes to continue with the game")
        a=input( "to see your cadrs please enter yes:")
    print(player_3.names ,"you have" ,player_3.coins, "coins")
    print(hiden_cards)
    print(hiden_cards)
    print(player_3.cards)
    print(hiden_cards)
    print(player_4.names, "it´s your time to play")
    a=input( "to see your cadrs please enter yes:")
    while a!= "yes":
        print(player_4.names, "please enter yes to continue with the game")
        a=input("to see your cadrs please enter yes:")
    print(player_4.names, "you have" ,player_4.coins, "coins")
    print(hiden_cards)
    print(hiden_cards)
    print(hiden_cards)
    print(player_4.cards)



if __name__ == "__main__":
    main()