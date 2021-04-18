import random
class Influences:
    def __init__(self):
        ...

"""
#ME ACABO DE DAR CUENTA QUE PUDE HABER HECHO 4 FUNCIONES Y TERMINABA LOS CHALLENGE EN 10 MIN Y EN MUCHO MENOS LINEAS :)
# DEF challenge_a... DEF challenge_b y asi... corregir mañana    
    def play(self,board,player_1,player_2,player_3,player_4):
        n_players = board.n_players
        turn = board.turn
        if n_players==4:
            if turn == 1:
                a = player_1
                b = player_2
                c = player_3
                d = player_4
            elif turn == 2:
                a = player_2
                b = player_3
                c = player_4
                d = player_1
            elif turn == 3:
                a = player_3
                b = player_4
                c = player_1
                d = player_2
            elif turn == 4:
                a = player_4
                b = player_1
                c = player_2
                d = player_3
            if turn==1:
                print(a.name)
                p_1=int(input ("wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid :"))
                if p_1==1:
                    print (a.name, "choose to play Duke")  
                elif p_1==2:
                    print (a.name, "choose to play Murderer") 
                elif p_1==3:
                    print(a.name ,"choose to play Captain")
                elif p_1==4:
                    print(a.name, "choose to play Ambassador")
                elif p_1==5:
                    print (a.name, "choose to play Coup")
                elif p_1==6:
                    print (a.name, "choose to play Income")
                else:
                    print(a.name ,"choose to play foreign aid")
                if p_1==2 or p_1==3:
                    print (a.name)
                    attack=input ("wich player do you whant to attack? :")
                    print (attack)
                else:
                    ...
                if p_1==1 or p_1==2 or p_1==3 or p_1==4:
                    print(b.name)
                    p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(c.name)
                    p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(d.name)
                    p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    list_challenge=[]
                    if p_2==1 and p_3==1 and p_4==1:
                        list_challenge.append(b.name)
                        list_challenge.append(c.name)
                        list_challenge.append(d.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                elif list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="DUKE":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                elif list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="MURDERER":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                elif list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="CAPTAIN":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                elif list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="AMBASSADOR":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                    elif p_2==1 and p_3==1:
                        list_challenge.append(b.name)
                        list_challenge.append(c.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else: 
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                if a.cards[0]=="DUKE":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                if a.cards[0]=="MURDERER":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else: 
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                if a.cards[0]=="CAPTAIN":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name, "just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                if a.cards[0]=="AMBASSADOR":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                    elif p_2==1 and p_4==1:
                        list_challenge.append(b.name)
                        list_challenge.append(d.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="DUKE":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else:
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                else:
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="MURDERER":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="CAPTAIN":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                else:
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="AMBASSADOR":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                    elif p_3==1 and p_4==1:
                        list_challenge.append(player_3.name)
                        list_challenge.append(player_4.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="DUKE":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else:
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="MURDERER":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else: 
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="CAPTAIN":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                else:
                                    print(d.name, "I´m sorry but you lose a card")
                                    print(d.cards, "this is(are) you(r) card(s)")
                                    if len(d.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(d.cards[0], "this is the card that", d.name, "just lost")
                                            d.vcards[0]=True
                                        else:
                                            print(d.cards[1], "this is the card that", d.name, "just lost")
                                            d.vcards[1]=True
                                    else:
                                        if d.vcards[0]==True:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[1])
                                            d.vcards[1]=True
                                        else:
                                            print(d.name,"I´m sorry but you lose, your last card was", d.cards[0])
                                            d.vcards[0]=True
                                if a.cards[0]=="AMBASSADOR":
                                    a.cards[0]=board.cards[0]
                                    print(a.name, "this is your new card",board.cards[0])
                                else:
                                    a.cards[0]=board.cards[1]
                                    print(a.name, "this is your new card",board.cards[1])
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(a.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(a.cards[0], "this is the card that", a.name, "just lost")
                                        a.vcards[0]=True
                                    else:
                                        print(a.cards[1], "this is the card that", a.name, "just lost")
                                        a.vcards[1]=True
                                else:
                                    if a.vcards[0]==True:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                        a.vcards[1]=True
                                    else:
                                        print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                        a.vcards[0]=True
                    elif p_2==1:
                        list_challenge.append(b)
                        print(b, "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="DUKE":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="MURDERER":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="CAPTAIN":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="AMBASSADOR":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        else:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="AMBASSADOR":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True 
                                                               
                            
                               
                        
                    elif p_3==1:
                        list_challenge.append(c)
                        print(c, "you do the challenge, good luck")
                        if p_1==1:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                    if a.cards[0]=="DUKE":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        elif p_1==2:
                            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==c.name:
                                    print(c.name, "I´m sorry but you lose a card")
                                    print(c.cards, "this is(are) you(r) card(s)")
                                    if len(c.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(c.cards[0], "this is the card that", c.name,"just lost")
                                            c.vcards[0]=True
                                        else:
                                            print(c.cards[1], "this is the card that", c.name, "just lost")
                                            c.vcards[1]=True
                                    else:
                                        if c.vcards[0]==True:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[1])
                                            c.vcards[1]=True
                                        else:
                                            print(c.name,"I´m sorry but you lose, your last card was", c.cards[0])
                                            c.vcards[0]=True
                                    if a.cards[0]=="MURDERER":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        elif p_1==3:
                            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="CAPTAIN":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        else:
                            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="AMBASSADOR":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True
                        else:
                            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]==b.name:
                                    print(b.name, "I´m sorry but you lose a card")
                                    print(b.cards, "this is(are) you(r) card(s)")
                                    if len(b.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(b.cards[0], "this is the card that", b.name,"just lost")
                                            b.vcards[0]=True
                                        else:
                                            print(b.cards[1], "this is the card that", b.name, "just lost")
                                            b.vcards[1]=True
                                    else:
                                        if b.vcards[0]==True:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[1])
                                            b.vcards[1]=True
                                        else:
                                            print(b.name,"I´m sorry but you lose, your last card was", b.cards[0])
                                            b.vcards[0]=True
                                    if a.cards[0]=="AMBASSADOR":
                                        a.cards[0]=board.cards[0]
                                        print(a.name, "this is your new card",board.cards[0])
                                    else:
                                        a.cards[0]=board.cards[1]
                                        print(a.name, "this is your new card",board.cards[1])
                                else:
                                    ...
                            else: 
                                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                                    if len(a.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(a.cards[0], "this is the card that", a.name, "just lost")
                                            a.vcards[0]=True
                                        else:
                                            print(a.cards[1], "this is the card that", a.name, "just lost")
                                            a.vcards[1]=True
                                    else:
                                        if a.vcards[0]==True:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[1])
                                            a.vcards[1]=True
                                        else:
                                            print(a.name,"I´m sorry but you lose, your last card was", a.cards[0])
                                            a.vcards[0]=True




                    elif p_4==1:
                        list_challenge.append(player_4.name)
                        print(player_4.name, "you do the challenge, good luck")
                    else:
                        list_challenge.append("no challenge")
                elif p_1==5:
                    player_1.coins-=7
                    k_o=input("wich player lose 1 influence :")
                    #hacer elegir al jugador atacado que carta pierde 
                elif p_1==6:
                    player_1.coins +=1
                else:
                    print("If someone whants to do a contra attack you will need the Duke")
                    print(player_2.name)
                    ask2=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    print(player_3.name)
                    ask3=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    print(player_3.name)
                    ask4=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    if ask2==2 and ask3==2 and ask4==2:
                        player_1.coins+=2
                    else:
                        if ask2==1:
                            ...#preguntar a los jugadores si quieren challenge
                        elif ask3==1: #agregar un and que la jugada no se haya cortado
                            ...#preguntar a los jugadores si quieren challenge
                        elif ask4==1: #agregar un and que la jugada no se haya cortado
                            ...#preguntar a los jugadores si quieren challenge
                        else:
                            player_1.coins+=2
                if p_1==2: 
                    player_1.coins -=3
                    print("To defense this attack you will need the Countess")
                    print(attack)
                    ask=int(input("Do you whant to defense? 1= yes 2= no :"))
                    if ask==2:
                        ...#hacer elegir que carta pierde
                    else:
                        ...#preguntar a los jugadores si quieren hacer un challenge 
                elif p_1==3:
                    print ("To defense this attack you will need the ambassador or the captain")
                    print (attack)
                    ask=int(input("Do you whant to defense? 1= yes 2= no :"))
                    if ask==2:
                        ...#hacer un if el jugador atacado tiene menos de 2 monedas robar 1 else robar 2
                    else:
                        ...#preguntar a los jugadores si quieren hacer un challenge 
                elif p_1==4:
                    ...#permitir ver dos cartas del mazo y elegir con cuales se queda
                elif p_1==1:
                    player_1.coins +=3
                else: 
                    ...
"""