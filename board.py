import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Board:
    def __init__(self, n_players, cards, turn, color):
        self.n_players = n_players
        self.cards = cards
        self.turn = turn
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value  

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
 

    def waiter(self,player):
        color = player.color[1]
        print(color)
        cls()
        print(" ░░███╗░░░░░░░░ ")
        print(" ░████║░░░░░░░░ ")
        print(" ██╔██║░░░░░░░░ ")
        print(" ╚═╝██║░░░░░░░░ ")
        print(" ███████╗██╗██╗ ")
        print(" ╚══════╝╚═╝╚═╝ ")
        time.sleep(1)
        cls()
        print(" ░░███╗░░░░░░░░  ██████╗░░░░░░░ ")
        print(" ░████║░░░░░░░░  ╚════██╗░░░░░░ ")
        print(" ██╔██║░░░░░░░░  ░░███╔═╝░░░░░░ ")
        print(" ╚═╝██║░░░░░░░░  ██╔══╝░░░░░░░░ ")
        print(" ███████╗██╗██╗  ███████╗██╗██╗ ")
        print(" ╚══════╝╚═╝╚═╝  ╚══════╝╚═╝╚═╝ ")
        time.sleep(1)
        cls()
        print(" ░░███╗░░░░░░░░  ██████╗░░░░░░░  ██████╗░░░░░░░ ")
        print(" ░████║░░░░░░░░  ╚════██╗░░░░░░  ╚════██╗░░░░░░ ")
        print(" ██╔██║░░░░░░░░  ░░███╔═╝░░░░░░  ░█████╔╝░░░░░░ ")
        print(" ╚═╝██║░░░░░░░░  ██╔══╝░░░░░░░░  ░╚═══██╗░░░░░░ ")
        print(" ███████╗██╗██╗  ███████╗██╗██╗  ██████╔╝██╗██╗ ")
        print(" ╚══════╝╚═╝╚═╝  ╚══════╝╚═╝╚═╝  ╚═════╝░╚═╝╚═╝ ")
        time.sleep(1)
        cls()
        print(" ░░███╗░░░░░░░░  ██████╗░░░░░░░  ██████╗░░░░░░░  ░░██╗██╗░░░░░░ ")
        print(" ░████║░░░░░░░░  ╚════██╗░░░░░░  ╚════██╗░░░░░░  ░██╔╝██║░░░░░░ ")
        print(" ██╔██║░░░░░░░░  ░░███╔═╝░░░░░░  ░█████╔╝░░░░░░  ██╔╝░██║░░░░░░ ")
        print(" ╚═╝██║░░░░░░░░  ██╔══╝░░░░░░░░  ░╚═══██╗░░░░░░  ███████║░░░░░░ ")
        print(" ███████╗██╗██╗  ███████╗██╗██╗  ██████╔╝██╗██╗  ╚════██║██╗██╗ ")
        print(" ╚══════╝╚═╝╚═╝  ╚══════╝╚═╝╚═╝  ╚═════╝░╚═╝╚═╝  ░░░░░╚═╝╚═╝╚═╝ ")
        time.sleep(1)
        cls()
        print(" ░░███╗░░░░░░░░  ██████╗░░░░░░░  ██████╗░░░░░░░  ░░██╗██╗░░░░░░  ███████╗░░░░░░")
        print(" ░████║░░░░░░░░  ╚════██╗░░░░░░  ╚════██╗░░░░░░  ░██╔╝██║░░░░░░  ██╔════╝░░░░░░")
        print(" ██╔██║░░░░░░░░  ░░███╔═╝░░░░░░  ░█████╔╝░░░░░░  ██╔╝░██║░░░░░░  ██████╗░░░░░░░")
        print(" ╚═╝██║░░░░░░░░  ██╔══╝░░░░░░░░  ░╚═══██╗░░░░░░  ███████║░░░░░░  ╚════██╗░░░░░░")
        print(" ███████╗██╗██╗  ███████╗██╗██╗  ██████╔╝██╗██╗  ╚════██║██╗██╗  ██████╔╝██╗██╗")
        print(" ╚══════╝╚═╝╚═╝  ╚══════╝╚═╝╚═╝  ╚═════╝░╚═╝╚═╝  ░░░░░╚═╝╚═╝╚═╝  ╚═════╝░╚═╝╚═╝")
        time.sleep(1)
        cls()

    def welcome(self,player_1,player_2,player_3,player_4):
        n_players = self.n_players
        print("It's time for players to see their cards")
        print("you have 3 seconds for memorize the cards")
        print("REMEMBER.. you only have 5 secs for change")
        print("the place with the other player.")
        if n_players == 4:
            print("so.. the first one will be "+player_1.name+" and the last "+player_4.name)
        else:
            print("so.. the first one will be "+player_1.name+" and the last "+player_3.name)
        time.sleep(8)
        name_1 = player_1.name #Name player 1
        x = 17-len(name_1)
        for i in range(x):
            name_1 += " "
        cards_1 = player_1.cards
        x1 = cards_1[0]
        x2 = cards_1[1]
        x = 10-len(x1)
        for i in range(x):
            x1 += " "

        x = 10-len(x2)
        for i in range(x):
            x2 += " "
        ca1 = x1+" -- "+x2 #Cards player 1
        self.waiter(player_1)
        cls()
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                         ┌────────────────────────┐                         ║")
        print("║                         │Name : "+name_1+       "│                         ║")
        print("║                         │       The Coup         │                         ║")
        print("║                         │"+ca1+                 "│                         ║")
        print("║                         └────────────────────────┘                         ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        time.sleep(3)
        name_2 = player_2.name #Name player 2
        x = 17-len(name_2)
        for i in range(x):
            name_2 += " "
        cards_2 = player_2.cards
        x1 = cards_2[0]
        x2 = cards_2[1]
        x = 10-len(x1)
        for i in range(x):
            x1 += " "

        x = 10-len(x2)
        for i in range(x):
            x2 += " "
        ca2 = x1+" -- "+x2 #Cards player 2
        self.waiter(player_2)
        cls()
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                         ┌────────────────────────┐                         ║")
        print("║                         │Name : "+name_2+       "│                         ║")
        print("║                         │       The Coup         │                         ║")
        print("║                         │"+ca2+                 "│                         ║")
        print("║                         └────────────────────────┘                         ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        time.sleep(3)
        name_3 = player_3.name #Name player 3
        x = 17-len(name_3)
        for i in range(x):
            name_3 += " "
        cards_3 = player_3.cards
        x1 = cards_3[0]
        x2 = cards_3[1]
        x = 10-len(x1)
        for i in range(x):
            x1 += " "

        x = 10-len(x2)
        for i in range(x):
            x2 += " "
        ca3 = x1+" -- "+x2 #Cards player 3
        self.waiter(player_3)
        cls()
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                         ┌────────────────────────┐                         ║")
        print("║                         │Name : "+name_3+       "│                         ║")
        print("║                         │       The Coup         │                         ║")
        print("║                         │"+ca3+                 "│                         ║")
        print("║                         └────────────────────────┘                         ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        time.sleep(3)
        if n_players == 4:
            name_4 = player_4.name #Name player 4
            x = 17-len(name_4)
            for i in range(x):
                name_4 += " "
            cards_4 = player_4.cards
            x1 = cards_4[0]
            x2 = cards_4[1]
            x = 10-len(x1)
            for i in range(x):
                x1 += " "

            x = 10-len(x2)
            for i in range(x):
                x2 += " "
            ca4 = x1+" -- "+x2 #Cards player 4
            self.waiter(player_4)
            cls()
            print("╔════════════════════════════════════════════════════════════════════════════╗")
            print("║                         ┌────────────────────────┐                         ║")
            print("║                         │Name : "+name_4+       "│                         ║")
            print("║                         │       The Coup         │                         ║")
            print("║                         │"+ca4+                 "│                         ║")
            print("║                         └────────────────────────┘                         ║")
            print("╚════════════════════════════════════════════════════════════════════════════╝")
            time.sleep(3)
        cls()
        print("\n")
        print("\033[1;37m"+"So lets begin the game :D!")
        time.sleep(2)
        cls()

    def showboard(self,player_1,player_2,player_3,player_4):
        n_players = self.n_players
        turn = self.turn

        a = player_1.color[0] #Colors
        b = player_2.color[0]
        c = player_3.color[0]
        d = player_4.color[0]
        e = self.color

        if turn == 1:
            a = player_1.color[1]
        elif turn == 2:
            b = player_2.color[1]
        elif turn == 3:
            c = player_3.color[1]
        else:
            d = player_4.color[1]




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
                c3 = str(coins_3)+"               "

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
            y1 = cards_2[0]
            y2 = cards_2[1]

            x = 10-len(y1)
            for i in range(x):
                y1 += " "

            x = 10-len(y2)
            for i in range(x):
                y2 += " "

            if v2 == [False,False]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca2 = y1+" - **********"

            elif v2 == [False,True]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - "+y2
            else: #Both cards are True
                ca2 = y1+" - "+y2


            cards_3 = player_3.cards
            v3 = player_3.vcards
            z1 = cards_3[0]
            z2 = cards_3[1]

            x = 10-len(z1)
            for i in range(x):
                z1 += " "

            x = 10-len(z2)
            for i in range(x):
                z2 += " "

            if v3 == [False,False]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - **********"
            elif v3 == [True,False]: #True: the card is reveled; False: the card is censored
                ca3 = z1+" - **********"

            elif v3 == [False,True]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - "+z2
            else: #Both cards are True
                ca3 = z1+" - "+z2


            cards_4 = player_4.cards
            v4 = player_4.vcards
            w1 = cards_4[0]
            w2 = cards_4[1]

            x = 10-len(w1)
            for i in range(x):
                w1 += " "

            x = 10-len(w2)
            for i in range(x):
                w2 += " "

            if v4 == [False,False]: #True: the card is reveled; False: the card is censored
                ca4 = "********** - **********"
            elif v4 == [True,False]: #True: the card is reveled; False: the card is censored
                ca4 = w1+" - **********"

            elif v4 == [False,True]: #True: the card is reveled; False: the card is censored
                ca4 = "********** - "+w2
            else: #Both cards are True
                ca4 = w1+" - "+w2


            if turn == 1:
                ca1 = x1+" - "+x2    
                print("") 
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+d+"┌───────────────────────┐                        "+c+"┌───────────────────────┐"+e+" ║")
                print("║ "+d+"│You need wait          │                        "+c+"│You need wait          │"+e+" ║")
                print("║ "+d+"│Name : "+name_4+      "│                        "+c+"│Name : "+name_3+      "│"+e+" ║")
                print("║ "+d+"│Coins: "+c4+          "│ "+c+"◄══════════════════════│Coins: "+c3+          "│"+e+" ║")
                print("║ "+d+"│"+ca4+                "│                        "+c+"│"+ca3+                "│"+e+" ║")
                print("║ "+d+"└───────────────────────┘                        "+c+"└───────────────────────┘"+e+" ║")
                print("║ "+d+"             ║                                                             "+e+"║")
                print("║ "+d+"             ▼                   "+e+"The Coup                    "+b+" ▲            "+e+"║")
                print("║                                                              "+b+" ║            "+e+"║")
                print("║ "+a+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+a+"│Your turn              │                        "+b+"│You are the next       │ "+e+"║")
                print("║ "+a+"│Name : "+name_1+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+a+"│Coins: "+c1+          "│══════════════════════► "+b+"│Coins: "+c2+          "│ "+e+"║")
                print("║ "+a+"│"+ca1+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+a+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("╚════════════════════════════════════════════════════════════════════════════╝")
            elif turn == 2:
                ca2 = y1+" - "+y2
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+d+"┌───────────────────────┐                        "+c+"┌───────────────────────┐ "+e+"║")
                print("║ "+d+"│You need wait          │                        "+c+"│You are the next       │ "+e+"║")
                print("║ "+d+"│Name : "+name_4+      "│                        "+c+"│Name : "+name_3+      "│ "+e+"║")
                print("║ "+d+"│Coins: "+c4+          "│ "+c+"◄══════════════════════│Coins: "+c3+          "│ "+e+"║")
                print("║ "+d+"│"+ca4+                "│                        "+c+"│"+ca3+                "│ "+e+"║")
                print("║ "+d+"└───────────────────────┘                        "+c+"└───────────────────────┘ "+e+"║")
                print("║ "+d+"             ║                                                             "+e+"║")
                print("║ "+d+"             ▼                   "+e+"The Coup                     "+b+"▲            "+e+"║")
                print("║                                                               "+b+"║            "+e+"║")
                print("║ "+a+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+a+"│You need wait          │                        "+b+"│Your turn              │ "+e+"║")
                print("║ "+a+"│Name : "+name_1+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+a+"│Coins: "+c1+          "│══════════════════════► "+b+"│Coins: "+c2+          "│ "+e+"║")
                print("║ "+a+"│"+ca1+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+a+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("╚════════════════════════════════════════════════════════════════════════════╝")
            elif turn ==3:
                ca3 = z1+" - "+z2
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+d+"┌───────────────────────┐                        "+c+"┌───────────────────────┐ "+e+"║")
                print("║ "+d+"│You are the next       │                        "+c+"│Your turn              │ "+e+"║")
                print("║ "+d+"│Name : "+name_4+      "│                        "+c+"│Name : "+name_3+      "│ "+e+"║")
                print("║ "+d+"│Coins: "+c4+          "│ "+c+"◄══════════════════════│Coins: "+c3+          "│ "+e+"║")
                print("║ "+d+"│"+ca4+                "│                        "+c+"│"+ca3+                "│ "+e+"║")
                print("║ "+d+"└───────────────────────┘                        "+c+"└───────────────────────┘ "+e+"║")
                print("║              "+d+"║                                                             "+e+"║")
                print("║              "+d+"▼                   "+e+"The Coup                     "+b+"▲            "+e+"║")
                print("║                                                               "+b+"║            "+e+"║")
                print("║ "+a+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+a+"│You need wait          │                        "+b+"│You need wait          │ "+e+"║")
                print("║ "+a+"│Name : "+name_1+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+a+"│Coins: "+c1+          "│══════════════════════► "+b+"│Coins: "+c2+          "│ "+e+"║")
                print("║ "+a+"│"+ca1+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+a+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("╚════════════════════════════════════════════════════════════════════════════╝")
            else:
                ca4 = w1+" - "+w2
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+d+"┌───────────────────────┐                        "+c+"┌───────────────────────┐ "+e+"║")
                print("║ "+d+"│Your turn              │                        "+c+"│You need wait          │ "+e+"║")
                print("║ "+d+"│Name : "+name_4+      "│                        "+c+"│Name : "+name_3+      "│ "+e+"║")
                print("║ "+d+"│Coins: "+c4+          "│ "+c+"◄══════════════════════│Coins: "+c3+          "│ "+e+"║")
                print("║ "+d+"│"+ca4+                "│                        "+c+"│"+ca3+                "│ "+e+"║")
                print("║ "+d+"└───────────────────────┘                        "+c+"└───────────────────────┘ "+e+"║")
                print("║              "+d+"║                                                             "+e+"║")
                print("║              "+d+"▼                   "+e+"The Coup                     "+b+"▲            "+e+"║")
                print("║                                                               "+b+"║            "+e+"║")
                print("║ "+a+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+a+"│You are the next       │                        "+b+"│You need wait          │ "+e+"║")
                print("║ "+a+"│Name : "+name_1+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+a+"│Coins: "+c1+          "│══════════════════════► "+b+"│Coins: "+c2+          "│ "+e+"║")
                print("║ "+a+"│"+ca1+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+a+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("╚════════════════════════════════════════════════════════════════════════════╝")
        elif n_players == 3:

            name_1 = player_1.name #Name player 1
            x = 16-len(name_1)
            for i in range(x+1):
                name_1 += " "

            name_2 = player_2.name #Name player 2
            x = 16-len(name_2)
            for i in range(x):
                name_2 += " "

            name_3 = player_3.name #Name player 3
            x = 16-len(name_3)
            for i in range(x):
                name_3 += " "


            coins_1 = player_1.coins #Coins of player 1
            if coins_1 >= 10:
                c1 = str(coins_1)+"               "
            else:
                c1 = str(coins_1)+"                "

            coins_2 = player_2.coins #Coins of player 2
            if coins_2 >= 10:
                c2 = str(coins_2)+"              "
            else:
                c2 = str(coins_2)+"               "

            coins_3 = player_3.coins #Coins of player 3
            if coins_3 >= 10:
                c3 = str(coins_3)+"              "
            else:
                c3 = str(coins_3)+"               "
            

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
                ca1 = "********** -- **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca1 = x1+" -- **********"

            elif v1 == [False,True]: #True: the card is reveled; False: the card is censored
                ca1 = "********** -- "+x2
            else: #Both cards are True
                ca1 = x1+" -- "+x2


            cards_2 = player_2.cards
            v2 = player_2.vcards
            y1 = cards_2[0]
            y2 = cards_2[1]

            x = 10-len(y1)
            for i in range(x):
                y1 += " "

            x = 10-len(y2)
            for i in range(x):
                y2 += " "

            if v2 == [False,False]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca2 = y1+" - **********"

            elif v2 == [False,True]: #True: the card is reveled; False: the card is censored
                ca2 = "********** - "+y2
            else: #Both cards are True
                ca2 = y1+" - "+y2


            cards_3 = player_3.cards
            v3 = player_3.vcards
            z1 = cards_3[0]
            z2 = cards_3[1]

            x = 10-len(z1)
            for i in range(x):
                z1 += " "

            x = 10-len(z2)
            for i in range(x):
                z2 += " "

            if v3 == [False,False]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - **********"
            elif v3 == [True,False]: #True: the card is reveled; False: the card is censored
                ca3 = z1+" - **********"

            elif v3 == [False,True]: #True: the card is reveled; False: the card is censored
                ca3 = "********** - "+z2
            else: #Both cards are True
                ca3 = z1+" - "+z2

            cards_4 = player_4.cards###
            v4 = player_4.vcards
            w1 = cards_4[0]
            w2 = cards_4[1]

            x = 10-len(w1)
            for i in range(x):
                w1 += " "

            x = 10-len(w2)
            for i in range(x):
                w2 += " " ###

            if turn == 1:
                ca1 = x1+" -- "+x2 
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+c+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+c+"│You need wait          │                        "+b+"│You are the next       │ "+e+"║")
                print("║ "+c+"│Name : "+name_3+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+c+"│Coins: "+c3+          "│   "+b+"◄════════════════════│Coins: "+c2+          "│ "+e+"║")
                print("║ "+c+"│"+ca3+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+c+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("║             "+c+"║                                                              "+e+"║")
                print("║             "+c+"║                    "+e+"The Coup                    "+a+"▲             "+e+"║")
                print("║             "+c+"║                                                "+a+"║             "+e+"║")
                print("║             "+c+"║           "+a+"┌────────────────────────┐           "+a+"║             "+e+"║")
                print("║             "+c+"║           "+a+"│Your turn               │           "+a+"║             "+e+"║")
                print("║             "+c+"║           "+a+"│Name : "+name_1+       "│           "+a+"║             "+e+"║")
                print("║             "+c+"╚═══════►   "+a+"│Coins: "+c1+           "│═══════════╝             "+e+"║")
                print("║                         "+a+"│"+ca1+                 "│                         "+e+"║")
                print("║                         "+a+"└────────────────────────┘                         "+e+"║")
                if(v4  == [True,True]):
                    ca4 = w1+" -- "+w2
                    print(""+e+"╚══════╗ Played Cards             ╔══════════════════════════════════════════╝")
                    print("       "+e+"║ "+d+""+ca4+                 " "+e+"║                                           ")
                    print("       ╚══════════════════════════╝                                           ")
                else:
                    print(""+e+"╚════════════════════════════════════════════════════════════════════════════╝")

            elif turn == 2:
                ca2 = y1+" - "+y2 
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+c+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+c+"│You are the next       │                        "+b+"│Your turn              │ "+e+"║")
                print("║ "+c+"│Name : "+name_3+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+c+"│Coins: "+c3+          "│   "+b+"◄════════════════════│Coins: "+c2+          "│ "+e+"║")
                print("║ "+c+"│"+ca3+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+c+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("║             "+c+"║                                                              "+e+"║")
                print("║             "+c+"║                    "+e+"The Coup                    "+a+"▲             "+e+"║")
                print("║             "+c+"║                                                "+a+"║             "+e+"║")
                print("║             "+c+"║           "+a+"┌────────────────────────┐           ║             "+e+"║")
                print("║             "+c+"║           "+a+"│You need wait           │           ║             "+e+"║")
                print("║             "+c+"║           "+a+"│Name : "+name_1+       "│           ║             "+e+"║")
                print("║             "+c+"╚═══════►   "+a+"│Coins: "+c1+           "│═══════════╝             "+e+"║")
                print("║                         "+a+"│"+ca1+                 "│                         "+e+"║")
                print("║                         "+a+"└────────────────────────┘                         "+e+"║")
                if(v4  == [True,True]):
                    ca4 = w1+" -- "+w2
                    print(""+e+"╚══════╗ Played Cards             ╔══════════════════════════════════════════╝")
                    print("       "+e+"║ "+d+""+ca4+                 " "+e+"║                                           ")
                    print("       ╚══════════════════════════╝                                           ")
                else:
                    print(""+e+"╚════════════════════════════════════════════════════════════════════════════╝")
            else:
                ca3 = z1+" - "+z2 
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║ "+c+"┌───────────────────────┐                        "+b+"┌───────────────────────┐ "+e+"║")
                print("║ "+c+"│Your turn              │                        "+b+"│You need wait          │ "+e+"║")
                print("║ "+c+"│Name : "+name_3+      "│                        "+b+"│Name : "+name_2+      "│ "+e+"║")
                print("║ "+c+"│Coins: "+c3+          "│   "+b+"◄════════════════════│Coins: "+c2+          "│ "+e+"║")
                print("║ "+c+"│"+ca3+                "│                        "+b+"│"+ca2+                "│ "+e+"║")
                print("║ "+c+"└───────────────────────┘                        "+b+"└───────────────────────┘ "+e+"║")
                print("║             "+c+"║                                                              "+e+"║")
                print("║             "+c+"║                    "+e+"The Coup                    "+a+"▲             "+e+"║")
                print("║             "+c+"║                                                "+a+"║             "+e+"║")
                print("║             "+c+"║           "+a+"┌────────────────────────┐           ║             "+e+"║")
                print("║             "+c+"║           "+a+"│You are the next        │           ║             "+e+"║")
                print("║             "+c+"║           "+a+"│Name : "+name_1+       "│           ║             "+e+"║")
                print("║             "+c+"╚═══════►   "+a+"│Coins: "+c1+           "│═══════════╝             "+e+"║")
                print("║                         "+a+"│"+ca1+                 "│                         "+e+"║")
                print("║                         "+a+"└────────────────────────┘                         "+e+"║")
                if(v4  == [True,True]):
                    ca4 = w1+" -- "+w2
                    print(""+e+"╚══════╗ Played Cards             ╔══════════════════════════════════════════╝")
                    print("       "+e+"║ "+d+""+ca4+                 " "+e+"║                                           ")
                    print("       "+e+"╚══════════════════════════╝                                           ")
                else:
                    print(""+e+"╚════════════════════════════════════════════════════════════════════════════╝")
        elif n_players == 2:

            name_1 = player_1.name #Name player 1
            x = 16-len(name_1)
            for i in range(x+1):
                name_1 += " "

            name_2 = player_2.name #Name player 2
            x = 16-len(name_2)
            for i in range(x+1):
                name_2 += " "

            coins_1 = player_1.coins #Coins of player 1
            if coins_1 >= 10:
                c1 = str(coins_1)+"               "
            else:
                c1 = str(coins_1)+"                "

            coins_2 = player_2.coins #Coins of player 2
            if coins_2 >= 10:
                c2 = str(coins_2)+"               "
            else:
                c2 = str(coins_2)+"                "

            

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
                ca1 = "********** -- **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca1 = x1+" -- **********"

            elif v1 == [False,True]: #True: the card is reveled; False: the card is censored
                ca1 = "********** -- "+x2
            else: #Both cards are True
                ca1 = x1+" -- "+x2


            cards_2 = player_2.cards
            v2 = player_2.vcards
            y1 = cards_2[0]
            y2 = cards_2[1]

            x = 10-len(y1)
            for i in range(x):
                y1 += " "

            x = 10-len(y2)
            for i in range(x):
                y2 += " "

            if v2 == [False,False]: #True: the card is reveled; False: the card is censored
                ca2 = "********** -- **********"
            elif v1 == [True,False]: #True: the card is reveled; False: the card is censored
                ca2 = y1+" -- **********"

            elif v2 == [False,True]: #True: the card is reveled; False: the card is censored
                ca2 = "********** -- "+y2
            else: #Both cards are True
                ca2 = y1+" -- "+y2

            cards_3 = player_3.cards###
            v3 = player_3.vcards
            z1 = cards_3[0]
            z2 = cards_3[1]

            x = 10-len(z1)
            for i in range(x):
                z1 += " "

            x = 10-len(z2)
            for i in range(x):
                z2 += " " ###

            cards_4 = player_4.cards###
            v4 = player_4.vcards
            w1 = cards_4[0]
            w2 = cards_4[1]

            x = 10-len(w1)
            for i in range(x):
                w1 += " "

            x = 10-len(w2)
            for i in range(x):
                w2 += " " ###

            if turn == 1:
                ca1 = x1+" -- "+x2
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║                         "+b+"┌────────────────────────┐                         "+e+"║")
                print("║                         "+b+"│You are the next        │                         "+e+"║")
                print("║            "+b+"╔════════════│Name : "+name_2+       "│    "+a+"◄═══════╗            "+e+"║")
                print("║            "+b+"║            │Coins: "+c2+           "│            "+a+"║            "+e+"║")
                print("║            "+b+"║            │"+ca2+                 "│            "+a+"║            "+e+"║")
                print("║            "+b+"║            └────────────────────────┘            "+a+"║            "+e+"║")
                print("║            "+b+"║                                                  "+a+"║            "+e+"║")
                print("║            "+b+"║                    "+e+"The Coup                      "+a+"║            "+e+"║")
                print("║            "+b+"║                                                  "+a+"║            "+e+"║")
                print("║            "+b+"║            "+a+"┌────────────────────────┐            ║            "+e+"║")
                print("║            "+b+"║            "+a+"│Your turn               │            ║            "+e+"║")
                print("║            "+b+"║            "+a+"│Name : "+name_1+       "│            ║            "+e+"║")
                print("║            "+b+"╚═══════►    "+a+"│Coins: "+c1+           "│════════════╝            "+e+"║")
                print("║                         "+a+"│"+ca1+                 "│                         "+e+"║")
                print("║                         "+a+"└────────────────────────┘                         "+e+"║")
                if (v3 == [True,True]) and (v4  == [True,True]):
                    ca3 = z1+" -- "+z2
                    ca4 = w1+" -- "+w2
                    print(""+e+"╚══════╗ Played Cards             ╔════════╗             Played Cards ╔══════╝")
                    print("       "+e+"║ "+c+""+ca3+                 " "+e+"║        ║ "+d+""+ca4+                 " "+e+"║       ")
                    print("       "+e+"╚══════════════════════════╝        ╚══════════════════════════╝       ")
                elif(v3  == [True,True]):
                    ca3 = z1+" -- "+z2
                    print(""+e+"╚══════╗ Played Cards             ╔══════════════════════════════════════════╝")
                    print("       "+e+"║ "+c+""+ca3+                 " "+e+"║                                           ")
                    print("       "+e+"╚══════════════════════════╝                                           ")

            else:
                ca2 = y1+" -- "+y2
                print("")
                print(""+e+"╔════════════════════════════════════════════════════════════════════════════╗")
                print("║                         "+b+"┌────────────────────────┐                         "+e+"║")
                print("║                         "+b+"│Your turn               │                         "+e+"║")
                print("║            "+b+"╔════════════│Name : "+name_2+       "│    "+a+"◄═══════╗            "+e+"║")
                print("║            "+b+"║            │Coins: "+c2+           "│            "+a+"║            "+e+"║")
                print("║            "+b+"║            │"+ca2+                 "│            "+a+"║            "+e+"║")
                print("║            "+b+"║            └────────────────────────┘            "+a+"║            "+e+"║")
                print("║            "+b+"║                                                  "+a+"║            "+e+"║")
                print("║            "+b+"║                    "+e+"The Coup                      "+a+"║            "+e+"║")
                print("║            "+b+"║                                                  "+a+"║            "+e+"║")
                print("║            "+b+"║            "+a+"┌────────────────────────┐            ║            "+e+"║")
                print("║            "+b+"║            "+a+"│You are the next        │            ║            "+e+"║")
                print("║            "+b+"║            "+a+"│Name : "+name_1+       "│            ║            "+e+"║")
                print("║            "+b+"╚═══════►    "+a+"│Coins: "+c1+           "│════════════╝            "+e+"║")
                print("║                         "+a+"│"+ca1+                 "│                         "+e+"║")
                print("║                         "+a+"└────────────────────────┘                         "+e+"║")
                if (v3 == [True,True]) and (v4  == [True,True]):
                    ca3 = z1+" -- "+z2
                    ca4 = w1+" -- "+w2
                    print(""+e+"╚══════╗ Played Cards             ╔════════╗             Played Cards ╔══════╝")
                    print("       "+e+"║ "+c+""+ca3+                 " "+e+"║        ║ "+d+""+ca4+                 " "+e+"║       ")
                    print("       "+e+"╚══════════════════════════╝        ╚══════════════════════════╝       ")
                elif(v3  == [True,True]):
                    ca3 = z1+" -- "+z2
                    print(""+e+"╚══════╗ Played Cards             ╔══════════════════════════════════════════╝")
                    print("       "+e+"║ "+c+""+ca3+                 " "+e+"║                                           ")
                    print("       "+e+"╚══════════════════════════╝                                           ")

        elif n_players == 1:

            name_1 = player_1.name #Name player 1
            x = 16-len(name_1)
            for i in range(x+1):
                name_1 += " "

            coins_1 = player_1.coins #Coins of player 1
            if coins_1 >= 10:
                c1 = str(coins_1)+"               "
            else:
                c1 = str(coins_1)+"                "

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

            ca1 = x1+" -- "+x2
            print("")
            print(""+a+"╔════════════════════════════════════════════════════════════════════════════╗")
            print("║ ┌────────────────────────────────────────────────────────────────────────┐ ║")
            print("║ │ *       *                                                  *       ✶   │ ║")
            print("║ │      ✶    ██╗       ██╗██╗███╗  ██╗███╗  ██╗███████╗██████╗            │ ║")
            print("║ │           ██║  ██╗  ██║██║████╗ ██║████╗ ██║██╔════╝██╔══██╗  °     ✶  │ ║")
            print("║ │  °        ╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗  ██████╔╝*          │ ║")
            print("║ │✶      ✶    ████╔═████║ ██║██║╚████║██║╚████║██╔══╝  ██╔══██╗        °  │ ║")
            print("║ │       °    ╚██╔╝ ╚██╔╝ ██║██║ ╚███║██║ ╚███║███████╗██║  ██║   ✶       │ ║")
            print("║ │          ╔══╩═╝   ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╩╗          │ ║")
            print("║ │    ✶     ║                                                  ║      *   │ ║")
            print("║ │          ║               ° ╗ of The Coup ╔ °                ║   °      │ ║")
            print("║ │       *  ║                 ╚═════════════╝                  ║       ✶  │ ║")
            print("║ │          ║            ┌────────────────────────┐            ║   *      │ ║")
            print("║ │ °        ║            │Name : "+name_1+       "│            ║          │ ║")
            print("║ │        ✶ ╚═══════►    │Coins: "+c1+           "│    ◄═══════╝     ✶    │ ║")
            print("║ │    ✶              *   │"+ca1+                 "│            °          │ ║")                
            print("║   *          °          └────────────────────────┘   ✶     *       *    °  ║")
            print("╚════════════════════════════════════════════════════════════════════════════╝")

    def evaluator(self,player_1,player_2,player_3,player_4):
        value = [True,True] #If someone have this lose the game

        nombre1 = player_1.name[:]
        nombre2 = player_2.name[:]
        nombre3 = player_3.name[:]
        nombre4 = player_4.name[:]

        ca1 = player_1.cards[:]
        ca2 = player_2.cards[:]
        ca3 = player_3.cards[:]
        ca4 = player_4.cards[:]

        vc1 = player_1.vcards[:]
        vc2 = player_2.vcards[:]
        vc3 = player_3.vcards[:]
        vc4 = player_4.vcards[:]

        co1 = (str(player_1.coins))[:]
        co2 = (str(player_2.coins))[:]
        co3 = (str(player_3.coins))[:]
        co4 = (str(player_4.coins))[:]

        col1 = player_1.color
        col2 = player_2.color
        col3 = player_3.color
        col4 = player_4.color

        n_players = self.n_players #Players
        turn = self.turn
        x = -1
        if n_players == 4:
            if vc1 == value:
                x = 1
                self.n_players -= 1
                player_1.name = nombre2
                player_2.name = nombre3
                player_3.name = nombre4
                player_4.name = nombre1
                player_1.cards = ca2
                player_2.cards = ca3
                player_3.cards = ca4
                player_4.cards = ca1
                player_1.vcards = vc2
                player_2.vcards = vc3
                player_3.vcards = vc4
                player_4.vcards = vc1
                player_1.coins = int(co2)
                player_2.coins = int(co3)
                player_3.coins = int(co4)
                player_4.coins = int(co1)
                player_1.color = col2
                player_2.color = col3
                player_3.color = col4
                player_4.color = col1
                if turn == 4:
                    self.turn = 1

            elif vc2 == value:
                x = 2
                self.n_players -= 1
                player_2.name = nombre3
                player_3.name = nombre4
                player_4.name = nombre2
                player_2.cards = ca3
                player_3.cards = ca4
                player_4.cards = ca2
                player_2.vcards = vc3
                player_3.vcards = vc4
                player_4.vcards = vc2
                player_2.coins = int(co3)
                player_3.coins = int(co4)
                player_4.coins = int(co2)
                player_2.color = col3
                player_3.color = col4
                player_4.color = col2
                if turn == 4:
                    self.turn = 1

            elif vc3 == value:
                x = 3
                self.n_players -= 1
                player_3.name = nombre4
                player_4.name = nombre3
                player_3.cards = ca4
                player_4.cards = ca3
                player_3.vcards = vc4
                player_4.vcards = vc3
                player_3.coins = int(co4)
                player_4.coins = int(co3)
                player_3.color = col4
                player_4.color = col3
                if turn == 4:
                    self.turn = 1

            elif vc4 == value:
                x = 4
                self.n_players -= 1
                self.turn = 1

            else:
                self.turn += 1
                if self.turn == 5:
                    self.turn = 1


            if turn < x:
                self.turn += 1
            if self.turn >= 5:
                self.turn = 1

        elif n_players == 3: #3 PLAYERS
            if vc1 == value:
                x = 1
                self.n_players -= 1
                player_1.name = nombre2
                player_2.name = nombre3
                player_3.name = nombre1
                player_1.cards = ca2
                player_2.cards = ca3
                player_3.cards = ca1
                player_1.vcards = vc2
                player_2.vcards = vc3
                player_3.vcards = vc1
                player_1.coins = int(co2)
                player_2.coins = int(co3)
                player_3.coins = int(co1)
                player_1.color = col2
                player_2.color = col3
                player_3.color = col1
                if turn == 3:
                    self.turn = 1

            elif vc2 == value:
                x = 2
                self.n_players -= 1
                player_2.name = nombre3
                player_3.name = nombre2
                player_2.cards = ca3
                player_3.cards = ca2
                player_2.vcards = vc3
                player_3.vcards = vc2
                player_2.coins = int(co3)
                player_3.coins = int(co2)
                player_2.color = col3
                player_3.color = col2
                if turn == 3:
                    self.turn = 1

            elif vc3 == value:
                x = 3
                self.n_players -= 1
                self.turn = 1

            else:
                self.turn += 1
                if self.turn == 4:
                    self.turn = 1

            if turn < x:
                self.turn += 1
            if self.turn >= 4:
                self.turn = 1

        elif n_players == 2:
            if vc1 == value:
                x = 1
                self.n_players -= 1
                player_1.name = nombre2
                player_2.name = nombre1
                player_1.cards = ca2
                player_2.cards = ca1
                player_1.vcards = vc2
                player_2.vcards = vc1
                player_1.coins = int(co2)
                player_2.coins = int(co1)
                player_1.color = col2
                player_2.color = col1
                if turn == 2:
                    self.turn = 1

            elif vc2 == value:
                x = 2
                self.n_players -= 1
                self.turn = 1

            else:
                self.turn += 1
                if self.turn == 3:
                    self.turn = 1

            if turn < x:
                self.turn += 1
            if self.turn >= 3:
                self.turn = 1
        
        self.showboard(player_1,player_2,player_3,player_4)



