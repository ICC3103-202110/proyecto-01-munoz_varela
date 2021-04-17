

class Board:
    
    def __init__(self, n_players, cards, turn):
        self.n_players = n_players
        self.cards = cards
        self.turn = turn

    @property
    def n_players(self):
        return self.__n_players

    @n_players.setter
    def n_players(self, value):
        self.__n_players = value

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        self.__cards = value
    
    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value
 

    def showboard(self,player_1,player_2,player_3,player_4):
        n_players = self.n_players
        turn = self.turn
        if n_players == 4:

            name_1 = player_1.name #Name player 1
            x = 16-len(name_1)
            for i in range(x):
                name_1 += " "

            name_2 = player_2.name #Name player 2
            x = 16-len(name_2)
            for i in range(x):
                name_2 += " "

            name_3 = player_3.name #Name player 3
            x = 16-len(name_3)
            for i in range(x):
                name_3 += " "

            name_4 = player_4.name #Name player 4
            x = 16-len(name_4)
            for i in range(x):
                name_4 += " "


            coins_1 = player_1.coins #Coins of player 1
            if coins_1 >= 10:
                c1 = str(coins_1)+"              "
            else:
                c1 = str(coins_1)+"               "

            coins_2 = player_2.coins #Coins of player 2
            if coins_2 >= 10:
                c2 = str(coins_2)+"              "
            else:
                c2 = str(coins_2)+"               "

            coins_3 = player_3.coins #Coins of player 3
            if coins_3 >= 10:
                c3 = str(coins_3)+"              "
            else:
                c3 = str(coins_2)+"               "

            coins_4 = player_4.coins #Coins of player 4
            if coins_4 >= 10:
                c4 = str(coins_4)+"              "
            else:
                c4 = str(coins_4)+"               "
            

            cards_1 = player_1.cards
            v1 = player_1.vcards
            x1 = cards_1[0]
            x2 = cards_1[1]

            x = 10-len(x1)
            for i in range(x):
                x1 += " "

            x = 10-len(x2)
            for i in range(x):
                x2 += " "

            if v1 == [False,False]: #True: the card is reveled; False: the card is censored
                ca1 = "********** - **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca1 = x1+" - **********"

            elif v1 == [False,True]: #True: the card is reveled; False: the card is censored
                ca1 = "********** - "+x2
            else: #Both cards are True
                ca1 = x1+" - "+x2


            cards_2 = player_2.cards
            v2 = player_2.vcards
            x1 = cards_2[0]
            x2 = cards_2[1]

            x = 10-len(x1)
            for i in range(x):
                x1 += " "

            x = 10-len(x2)
            for i in range(x):
                x2 += " "

            if v2 == [False,False]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca2 = x1+" - **********"

            elif v2 == [False,True]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - "+x2
            else: #Both cards are True
                ca2 = x1+" - "+x2


            cards_3 = player_3.cards
            v3 = player_3.vcards
            x1 = cards_3[0]
            x2 = cards_3[1]

            x = 10-len(x1)
            for i in range(x):
                x1 += " "

            x = 10-len(x2)
            for i in range(x):
                x2 += " "

            if v3 == [False,False]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - **********"
            elif v3 == [True,False]: #True: the card is reveled; False: the card is censored
                ca3 = x1+" - **********"

            elif v3 == [False,True]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - "+x2
            else: #Both cards are True
                ca3 = x1+" - "+x2


            cards_4 = player_4.cards
            v4 = player_4.vcards
            x1 = cards_4[0]
            x2 = cards_4[1]

            x = 10-len(x1)
            for i in range(x):
                x1 += " "

            x = 10-len(x2)
            for i in range(x):
                x2 += " "

            if v4 == [False,False]: #True: the card is reveled; False: the card is censored
                ca4 = "********** - **********"
            elif v4 == [True,False]: #True: the card is reveled; False: the card is censored
                ca4 = x1+" - **********"

            elif v4 == [False,True]: #True: the card is reveled; False: the card is censored
                ca4 = "********** - "+x2
            else: #Both cards are True
                ca4 = x1+" - "+x2


            if turn == 1:
                ca1 = x1+" - "+x2    
                print("╔══════════════════════════════════════════════════════════════════════════╗")
                print("║┌───────────────────────┬────────────────────────┬───────────────────────┐║")
                print("║│You need wait          │                        │You need wait          │║")
                print("║│Name : "+name_4+      "│                        │Name : "+name_3+      "│║")
                print("║│Coins: "+c4+          "│           ◄◄           │Coins: "+c3+          "│║")
                print("║│"+ca4+                "│                        │"+ca3+                "│║")
                print("║├───────────────────────┘                        └───────────────────────┤║")
                print("║│                                                                        │║")
                print("║│            ▼                     COUP                       ▲          │║")
                print("║│                                                                        │║")
                print("║├───────────────────────┐                        ┌───────────────────────┤║")
                print("║│Your turn              │                        │You are the next       │║")
                print("║│Name : "+name_1+      "│                        │Name : "+name_2+      "│║")
                print("║│Coins: "+c1+          "│           ►►           │Coins: "+c2+          "│║")
                print("║│"+ca1+                "│                        │"+ca2+                "│║")
                print("║└───────────────────────┴────────────────────────┴───────────────────────┘║")
                print("╚══════════════════════════════════════════════════════════════════════════╝")
            elif turn == 2:
                ca2 = x1+" - "+x2
                print("╔══════════════════════════════════════════════════════════════════════════╗")
                print("║┌───────────────────────┬────────────────────────┬───────────────────────┐║")
                print("║│You need wait          │                        │You are the next       │║")
                print("║│Name : "+name_4+      "│                        │Name : "+name_3+      "│║")
                print("║│Coins: "+c4+          "│           ◄◄           │Coins: "+c3+          "│║")
                print("║│"+ca4+                "│                        │"+ca3+                "│║")
                print("║├───────────────────────┘                        └───────────────────────┤║")
                print("║│                                                                        │║")
                print("║│            ▼                     COUP                       ▲          │║")
                print("║│                                                                        │║")
                print("║├───────────────────────┐                        ┌───────────────────────┤║")
                print("║│You need wait          │                        │You turn               │║")
                print("║│Name : "+name_1+      "│                        │Name : "+name_2+      "│║")
                print("║│Coins: "+c1+          "│           ►►           │Coins: "+c2+          "│║")
                print("║│"+ca1+                "│                        │"+ca2+                "│║")
                print("║└───────────────────────┴────────────────────────┴───────────────────────┘║")
                print("╚══════════════════════════════════════════════════════════════════════════╝")
            elif turn ==3:
                ca3 = x1+" - "+x2
                print("╔══════════════════════════════════════════════════════════════════════════╗")
                print("║┌───────────────────────┬────────────────────────┬───────────────────────┐║")
                print("║│You are the next       │                        │You turn               │║")
                print("║│Name : "+name_4+      "│                        │Name : "+name_3+      "│║")
                print("║│Coins: "+c4+          "│           ◄◄           │Coins: "+c3+          "│║")
                print("║│"+ca4+                "│                        │"+ca3+                "│║")
                print("║├───────────────────────┘                        └───────────────────────┤║")
                print("║│                                                                        │║")
                print("║│            ▼                     COUP                       ▲          │║")
                print("║│                                                                        │║")
                print("║├───────────────────────┐                        ┌───────────────────────┤║")
                print("║│You need wait          │                        │You need wait          │║")
                print("║│Name : "+name_1+      "│                        │Name : "+name_2+      "│║")
                print("║│Coins: "+c1+          "│           ►►           │Coins: "+c2+          "│║")
                print("║│"+ca1+                "│                        │"+ca2+                "│║")
                print("║└───────────────────────┴────────────────────────┴───────────────────────┘║")
                print("╚══════════════════════════════════════════════════════════════════════════╝")
            else:
                ca4 = x1+" - "+x2
                print("╔══════════════════════════════════════════════════════════════════════════╗")
                print("║┌───────────────────────┬────────────────────────┬───────────────────────┐║")
                print("║│You turn               │                        │You need wait          │║")
                print("║│Name : "+name_4+      "│                        │Name : "+name_3+      "│║")
                print("║│Coins: "+c4+          "│           ◄◄           │Coins: "+c3+          "│║")
                print("║│"+ca4+                "│                        │"+ca3+                "│║")
                print("║├───────────────────────┘                        └───────────────────────┤║")
                print("║│                                                                        │║")
                print("║│            ▼                     COUP                       ▲          │║")
                print("║│                                                                        │║")
                print("║├───────────────────────┐                        ┌───────────────────────┤║")
                print("║│You are the next       │                        │You need wait          │║")
                print("║│Name : "+name_1+      "│                        │Name : "+name_2+      "│║")
                print("║│Coins: "+c1+          "│           ►►           │Coins: "+c2+          "│║")
                print("║│"+ca1+                "│                        │"+ca2+                "│║")
                print("║└───────────────────────┴────────────────────────┴───────────────────────┘║")
                print("╚══════════════════════════════════════════════════════════════════════════╝")
