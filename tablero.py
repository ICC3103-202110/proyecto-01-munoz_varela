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
