import random
class Influences:
    def __init__(self):
        ...
################################  MURDERER   ################################
    def challenge_MURDERER(self,board,a,b,c,d,attack):
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                print(a.name,"you didn´t lie, you have MURDERER!")
                if a.cards[0]=="MURDERER":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(a.name, "this is your new card",a.cards[0])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if attack==b.name:
                            print(b.name,"you are out of the game")
                            b.vcards[0]=True
                            b.vcareds[1]=True
                        else:
                            if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if attack==c.name:
                            print(c.name,"you are out of the game")
                            c.vcards[0]=True
                            c.vcareds[1]=True
                        else:
                            if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if attack==d.name:
                            print(d.name,"you are out of the game")
                            d.vcards[0]=True
                            d.vcareds[1]=True
                        else:
                            if d.vcards[0]==False and d.vcards[1]==False:
                                delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(d.cards[0], "this is the card that", d.name,"just lost")
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
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(a.name, "this is your new card",a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if attack==b.name:
                            print(b.name,"you are out of the game")
                            b.vcards[0]=True
                            b.vcareds[1]=True
                        else:
                            if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if attack==c.name:
                            print(c.name,"you are out of the game")
                            c.vcards[0]=True
                            c.vcareds[1]=True
                        else:
                            if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if attack==d.name:
                            print(d.name,"you are out of the game")
                            d.vcards[0]=True
                            d.vcareds[1]=True
                        else:
                            if d.vcards[0]==False and d.vcards[1]==False:
                                delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="MURDERER":
                print(a.name,"you didn´t lie, you have the MURDERER!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="MURDERER"
                print(a.name, "this is your new card",a.cards[1])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if attack==b.name:
                        print(b.name,"you are out of the game")
                        b.vcards[0]=True
                        b.vcareds[1]=True
                    else:
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if attack==c.name:
                        print(c.name,"you are out of the game")
                        c.vcards[0]=True
                        c.vcareds[1]=True
                    else:
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if attack==d.name:
                        print(d.name,"you are out of the game")
                        d.vcards[0]=True
                        d.vcareds[1]=True
                    else:
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="MURDERER":
                print(a.name,"you didn´t lie, you have the MURDERER!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="MURDERER"
                print(a.name, "this is your new card",a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if attack==b.name:
                        print(b.name,"you are out of the game")
                        b.vcards[0]=True
                        b.vcareds[1]=True
                    else:
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if attack==c.name:
                        print(c.name,"you are out of the game")
                        c.vcards[0]=True
                        c.vcareds[1]=True
                    else:
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if attack==d.name:
                        print(d.name,"you are out of the game")
                        d.vcards[0]=True
                        d.vcareds[1]=True
                    else:
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
            ...
################################  COUNTESS   ################################
    def challenge_COUNTESS(self,board,a,b,c,d):
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="COUNTESS" or a.cards[1]=="COUNTESS":
                print(a.name,"you didn´t lie, you have the COUNTESS!")
                if a.cards[0]=="COUNTESS":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="COUNTESS"
                    print(a.name, "this is your new card",a.cards[0])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="COUNTESS"
                    print(a.name, "this is your new card",a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :(")
                print (a.name, "you are out of the game :(")
                a.vcards[0]=True 
                a.vcards[1]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="COUNTESS":
                print(a.name,"you didn´t lie, you have the COUNTESS!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="COUNTESS"
                print(a.name, "this is your new card",a.cards[1])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie")
                print (a.name, "you are out of the game :(")
                a.vcards[0]=True 
                a.vcards[1]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="COUNTESS":
                print(a.name,"you didn´t lie, you have the COUNTESS!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="COUNTESS"
                print(a.name, "this is your new card",a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie")
                print (a.name, "you are out of the game :(")
                a.vcards[0]=True 
                a.vcards[1]=True
        else:
            ...
################################    DUKE     ################################
    def challenge_DUKE(self,board,a,b,c,d):
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                    print(a.name,"you didn´t lie, you have the DUKE!")
                if a.cards[0]=="DUKE":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="DUKE"
                    print(a.name, "this is your new card",a.cards[0])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="DUKE"
                    print(a.name, "this is your new card",a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="DUKE":
                print(a.name,"you didn´t lie, you have the DUKE!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="DUKE"
                print(a.name, "this is your new card",a.cards[1])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="DUKE":
                print(a.name,"you didn´t lie, you have the DUKE!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="DUKE"
                print(a.name, "this is your new card",a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
            ...
################################   CAPTAIN   ################################
    def challenge_CAPTAIN(self,board,a,b,c,d):
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                    print(a.name,"you didn´t lie, you have the CAPTAIN!")
                if a.cards[0]=="CAPTAIN":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="CAPTAIN"
                    print(a.name, "this is your new card",a.cards[0])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="CAPTAIN"
                    print(a.name, "this is your new card",a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="CAPTAIN":
                print(a.name,"you didn´t lie, you have the CAPTAIN!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="CAPTAIN"
                print(a.name, "this is your new card",a.cards[1])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="CAPTAIN":
                print(a.name,"you didn´t lie, you have the CAPTAIN!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="CAPTAIN"
                print(a.name, "this is your new card",a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
            ...
################################ AMBASSADOR  ################################  
    def challenge_AMBASSADOR(self,board,a,b,c,d):
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                print(a.name,"you didn´t lie, you have the AMBASSADOR!")
                if a.cards[0]=="AMBASSADOR":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="AMBASSADOR"
                    print(a.name, "this is your new card",a.cards[0])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="AMBASSADOR"
                    print(a.name, "this is your new card",a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        print(list_challenge[0], "you lose the challenge")
                        print(d.name, "I´m sorry but you lose a card")
                        print(d.cards, "this is(are) you(r) card(s)")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="AMBASSADOR":
                print(a.name,"you didn´t lie, you have the AMBASSADOR!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="AMBASSADOR"
                print(a.name, "this is your new card",a.cards[1])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="AMBASSADOR":
                print(a.name,"you didn´t lie, you have the AMBASSADOR!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="AMBASSADOR"
                print(a.name, "this is your new card",a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(b.name, "I´m sorry but you lose a card")
                    print(b.cards, "this is(are) you(r) card(s)")
                    if b.vcards[0]==False and b.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(c.name, "I´m sorry but you lose a card")
                    print(c.cards, "this is(are) you(r) card(s)")
                    if c.vcards[0]==False and c.vcards[1]==False:
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
                    print(list_challenge[0], "you lose the challenge")
                    print(d.name, "I´m sorry but you lose a card")
                    print(d.cards, "this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(d.cards[0], "this is the card that", d.name,"just lost")
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
                print (a.name,"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
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
            ...
################################  PLAY GAME  ################################    
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
            
            turn = 1
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
                        #poner las funciones segun corresponda en los casos que corresponda
                    elif p_2==1 and p_3==1:
                        ...
                    elif p_2==1 and p_4==1:
                        ...
                    elif p_3==1 and p_4==1:
                        ...
                    elif p_2==1:
                        ...
                    elif p_3==1:
                        ...
                    elif p_4==1:
                        list_challenge.append(player_4.name)
                        print(player_4.name, "you do the challenge, good luck")
                    else:
                        list_challenge.append("no challenge")
                elif p_1==5:
                    a.coins-=7
                    k_o=input("wich player lose 1 influence :")
                    #hacer elegir al jugador atacado que carta pierde
                    if k_o==b.name:
                        print(b.name, "I´m sorry but you lose a card")
                        print(b.cards, "this is(are) you(r) card(s)")
                        if b.vcards[0]==False and b.vcards[1]==False:
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
                    elif k_o==c.name:
                        print(c.name, "I´m sorry but you lose a card")
                        print(c.cards, "this is(are) you(r) card(s)")
                        if c.vcards[0]==False and c.vcards[1]==False:
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
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input("Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(d.cards[0], "this is the card that", d.name,"just lost")
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
                elif p_1==6:
                    a.coins +=1
                else:
                    print("If someone whants to do a contra attack you will need the Duke")
                    print(b.name)
                    ask2=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    print(c.name)
                    ask3=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    print(d.name)
                    ask4=int(input("Do you whant to contra attack? 1= yes 2= no :"))
                    if ask2==2 and ask3==2 and ask4==2:
                        player_1.coins+=2
                    else:
                        if ask2==1:
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can have the two coins")
                            else:
                                print("we have a challenge!")
                                #hacer challenge
                        elif ask3==1: #hacer condicion de si hay challenge y pierde que pase a este
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can have the two coins")
                            else:
                                print("we have a challenge!")
                        elif ask4==1: 
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can have the two coins")
                            else:
                                print("we have a challenge!")
                        else: #si se hacen los challenge y gana el challenge player 1
                            a.coins+=2
                if p_1==2: 
                    a.coins -=3
                    print("To defense this attack you will need the Countess")
                    print(attack)
                    ask=int(input("Do you whant to defense? 1= yes 2= no :"))
                    if ask==2:
                        if attack==b.name:
                            print(b.name, "I´m sorry but you lose a card")
                            print(b.cards, "this is(are) you(r) card(s)")
                            if b.vcards[0]==False and b.vcards[1]==False:
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
                        elif attack==c.name:
                            print(c.name, "I´m sorry but you lose a card")
                            print(c.cards, "this is(are) you(r) card(s)")
                            if c.vcards[0]==False and c.vcards[1]==False:
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
                            if d.vcards[0]==False and d.vcards[1]==False:
                                delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(d.cards[0], "this is the card that", d.name,"just lost")
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
                        if attack==b.name:
                            print(b.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack")
                            else:
                                print("we have a challenge!")
                        elif attack==c.name:
                            print(c.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack")
                            else:
                                print("we have a challenge!")
                        else:
                            print(d.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack ")
                            else:
                                print("we have a challenge!")
                elif p_1==3:
                    print ("To defense this attack you will need the ambassador or the captain")
                    print (attack)                
                    ask=int(input("Do you whant to defense? 1= yes 2= no :"))
                    if ask==2:
                        if attack==b.name:
                            if b.coins>=2:
                                b.coins-=2
                                a.coins+=2
                                print("sorry",b.name,"but",a.name,"take 2 of your coins")
                            elif b.coins==1:
                                b.coins-=1
                                a.coins+=1
                                print("sorry",b.name,"but",a.name,"take the last coin you have")
                            else:
                                print(a.name,"bad call...", b.name,"don´t have coins...")
                        elif attack==c.name:
                            if c.coins>=2:
                                c.coins-=2
                                a.coins+=2
                                print("sorry",c.name,"but",a.name,"take 2 of your coins")
                            elif c.coins==1:
                                c.coins-=1
                                a.coins+=1
                                print("sorry",c.name,"but",a.name,"take the last coin you have")
                            else:
                                print(a.name,"bad call...", c.name,"don´t have coins...")
                        else:
                            if d.coins>=2:
                                d.coins-=2
                                a.coins+=2
                                print("sorry",d.name,"but",a.name,"take 2 of your coins")
                            elif d.coins==1:
                                d.coins-=1
                                a.coins+=1
                                print("sorry",d.name,"but",a.name,"take the last coin you have")
                            else:
                                print(a.name,"bad call...", d.name,"don´t have coins...")
                    else:
                        if attack==b.name:
                            print(b.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack")
                            else:
                                print("we have a challenge!")
                        elif attack==c.name:
                            print(c.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(d.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack")
                            else:
                                print("we have a challenge!")
                        else:
                            print(d.name,"use the defense")
                            print(a.name)
                            p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(b.name)
                            p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            print(c.name)
                            p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                            if p_2==2 and p_3==2 and p_4==2:
                                print ("I´m sorry", a.name, "but you can´t do your attack ")
                            else:
                                print("we have a challenge!") 
                elif p_1==4:
                    print(b.name)
                    p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(c.name)
                    p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(d.name)
                    p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    if p_2==2 and p_3==2 and p_4==2:
                        print(a.name,"you can choose 2 cards between your own cards and 2 of the desk")
                        if a.vcards[0]==False and a.vcards[1]==False:
                            print("this are the cards, you have to choose 1 each time")
                            print(a.cards[0],"=1",a.cards[1],"=2",board.cards[0],"=3",board.cards[1],"=4")
                            value_1=int (input("enter the frist card that you want, JUST the frist one:"))
                            value_2=int (input("now enter the second card that you want :"))
                            while value_1==value_2:
                                print("you can´t choose", value_1,"and",value_2,"please make them different")
                                value_1=int (input("enter the frist card that you want, JUST the frist one:"))
                                value_2=int (input("now enter the second card that you want :"))
                            if value_1==2:
                                a.cards[0]=a.cards[1]
                            elif value_1==3:
                                help_issue=a.cards[0]
                                a.cards[0]=board.cards[0]
                                board.cards[6]=help_issue
                            elif value_1==4:
                                help_issue=a.cards[0]
                                a.cards[0]=board.cards[1]
                                board.cards[6]=help_issue
                            elif value_2==1:
                                a.cards[1]=a.cards[0]
                            elif value_2==3:
                                help_issue=a.cards[1]
                                a.cards[1]=board.cards[0]
                                board.cards[6]=help_issue
                            elif value_2==4:
                                help_issue=a.cards[1]
                                a.cards[1]=board.cards[1]
                                board.cards[6]=help_issue
                            else:
                                ...
                            print(a.name, "this are your cards after your choice:")
                            print(a.cards)
                        else:
                            print(a.name,"you can choose 1 cards between your own card and 2 of the desk")
                            print("this are the cards, you have to choose 1")
                            if a.vcards[0]==True:
                                print(a.cards[1],"=1",board.cards[0],"=3",board.cards[1],"=4")
                                value_1=int (input("Wich card do you want? (1,2,3):"))
                                if value_1==2:
                                    help_issue=a.cards[1]
                                    a.cards[1]=board.cards[0]
                                    board.cards[6]=help_issue
                                elif value_1==3:
                                    help_issue=a.cards[1]
                                    a.cards[1]=board.cards[1]
                                    board.cards[6]=help_issue
                                else:
                                    ...
                            else:
                                print(a.cards[1],"=1",board.cards[0],"=3",board.cards[1],"=4")
                                value_1=int (input("Wich card do you want? (1,2,3):"))
                                if value_1==2:
                                    help_issue=a.cards[0]
                                    a.cards[0]=board.cards[0]
                                    board.cards[6]=help_issue
                                elif value_1==3:
                                    help_issue=a.cards[0]
                                    a.cards[0]=board.cards[1]
                                    board.cards[6]=help_issue
                                else:
                                    ...

                elif p_1==1:
                    print(b.name)
                    p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(c.name)
                    p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(d.name)
                    p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    if p_2==2 and p_3==2 and p_4==2:
                        print(a.name,"good for you! you earn 3 coins")
                        player_1.coins +=3
                    else:
                        ...
                else: 
                    ...
