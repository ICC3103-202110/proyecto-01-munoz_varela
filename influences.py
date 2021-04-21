import random

def cond(board,player_1,player_2,player_3,player_4):
    turn = board.turn
    E = "\033[0;37m"
    if turn == 1:
        A = player_1.color[1]
        B = player_2.color[1]
        C = player_3.color[1]
        D = player_4.color[1]
        a = player_1
        b = player_2
        c = player_3
        d = player_4
    elif turn == 2:
        A = player_2.color[1]
        B = player_3.color[1]
        C = player_4.color[1]
        D = player_1.color[1]
        a = player_2
        b = player_3
        c = player_4
        d = player_1
    elif turn == 3:
        A = player_3.color[1]
        B = player_4.color[1]
        C = player_1.color[1]
        D = player_2.color[1]
        a = player_3
        b = player_4
        c = player_1
        d = player_2
    elif turn == 4:
        A = player_4.color[1]
        B = player_1.color[1]
        C = player_2.color[1]
        D = player_3.color[1]
        a = player_4
        b = player_1
        c = player_2
        d = player_3
    return A,B,C,D,E,a,b,c,d

class Influences:
#################################  MURDERER   #################################
    def challenge_MURDERER(self,board,player_1,player_2,player_3,player_4,list_challenge):
        A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have MURDERER!")
                if a.cards[0]=="MURDERER":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if attack==b.name:
                            print(B+b.name,""+E+"you are out of the game")
                            b.vcards[0]=True
                            b.vcareds[1]=True
                        else:
                            if b.vcards[0]==False and b.vcards[1]==False:
                                print(B+b.cards[0], b.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                    b.vcards[0]=True
                                else:
                                    print(b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                    b.vcards[1]=True
                            else:
                                if b.vcards[0]==True:
                                    print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                    b.vcards[1]=True
                                else:
                                    print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                    b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if attack==c.name:
                            print(C+c.name,""+E+"you are out of the game")
                            c.vcards[0]=True
                            c.vcareds[1]=True
                        else:
                            if c.vcards[0]==False and c.vcards[1]==False:
                                print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(c.cards[0], ""+E+"this is the card that", C+c.name,"just lost")
                                    c.vcards[0]=True
                                else:
                                    print(c.cards[1], ""+E+"this is the card that", C+c.name, "just lost")
                                    c.vcards[1]=True
                            else:
                                if c.vcards[0]==True:
                                    print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                    c.vcards[1]=True
                                else:
                                    print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                    c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if attack==d.name:
                            print(D+d.name,""+E+"you are out of the game")
                            d.vcards[0]=True
                            d.vcareds[1]=True
                        else:
                            if d.vcards[0]==False and d.vcards[1]==False:
                                print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                    d.vcards[0]=True
                                else:
                                    print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                    d.vcards[1]=True
                            else:
                                if d.vcards[0]==True:
                                    print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                    d.vcards[1]=True
                                else:
                                    print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                    d.vcards[0]=True
                else:
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[1])
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if attack==b.name:
                            print(B+b.name,""+E+"you are out of the game")
                            b.vcards[0]=True
                            b.vcareds[1]=True
                        else:
                            if b.vcards[0]==False and b.vcards[1]==False:
                                print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                    b.vcards[0]=True
                                else:
                                    print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                    b.vcards[1]=True
                            else:
                                if b.vcards[0]==True:
                                    print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                    b.vcards[1]=True
                                else:
                                    print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                    b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if attack==c.name:
                            print(C+c.name,""+E+"you are out of the game")
                            c.vcards[0]=True
                            c.vcareds[1]=True
                        else:
                            if c.vcards[0]==False and c.vcards[1]==False:
                                print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                    c.vcards[0]=True
                                else:
                                    print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                    c.vcards[1]=True
                            else:
                                if c.vcards[0]==True:
                                    print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                    c.vcards[1]=True
                                else:
                                    print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                    c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if attack==d.name:
                            print(D+d.name,""+E+"you are out of the game")
                            d.vcards[0]=True
                            d.vcareds[1]=True
                        else:
                            if d.vcards[0]==False and d.vcards[1]==False:
                                print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                                delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                                if delete==1:
                                    print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                    d.vcards[0]=True
                                else:
                                    print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                    d.vcards[1]=True
                            else:
                                if d.vcards[0]==True:
                                    print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                    d.vcards[1]=True
                                else:
                                    print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                    d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2 
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="MURDERER":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the MURDERER!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="MURDERER"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if attack==b.name:
                        print(B+b.name,""+E+"you are out of the game")
                        b.vcards[0]=True
                        b.vcareds[1]=True
                    else:
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if attack==c.name:
                        print(C+c.name,""+E+"you are out of the game")
                        c.vcards[0]=True
                        c.vcareds[1]=True
                    else:
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                    if attack==d.name:
                        print(D+d.name,""+E+"you are out of the game")
                        d.vcards[0]=True
                        d.vcareds[1]=True
                    else:
                        if d.vcards[0]==False and d.vcards[1]==False:
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", E+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", E+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1])
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0])
                        a.vcards[0]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="MURDERER":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the MURDERER!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="MURDERER"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if attack==b.name:
                        print(B+b.name,""+E+"you are out of the game")
                        b.vcards[0]=True
                        b.vcareds[1]=True
                    else:
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if attack==c.name:
                        print(C+c.name,""+E+"you are out of the game")
                        c.vcards[0]=True
                        c.vcareds[1]=True
                    else:
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(c.cards[1], "this is the card that", c.name, "just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if attack==d.name:
                        print(D+d.name,""+E+"you are out of the game")
                        d.vcards[0]=True
                        d.vcareds[1]=True
                    else:
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        else:
            ...
#################################  COUNTESS   #################################
    def challenge_COUNTESS(self,board,player_1,player_2,player_3,player_4,list_challenge):
        A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="COUNTESS" or a.cards[1]=="COUNTESS":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the COUNTESS!")
                if a.cards[0]=="COUNTESS":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="COUNTESS"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1])
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0])
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], "you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
                else:                    
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="COUNTESS"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :(")
                win_challenge=2
                print (A+a.name, ""+E+"you are out of the game :(")
                a.vcards[0]=True 
                a.vcards[1]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="COUNTESS":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the COUNTESS!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="COUNTESS"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie")
                win_challenge=2
                print (A+a.name, ""+E+"you are out of the game :(")
                a.vcards[0]=True 
                a.vcards[1]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="COUNTESS":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the COUNTESS!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="COUNTESS"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie")
                print (A+a.name, ""+E+"you are out of the game :(")
                win_challenge=2
                a.vcards[0]=True 
                a.vcards[1]=True
        else:
            ...
#################################    DUKE     #################################
    def challenge_DUKE(self,board,player_1,player_2,player_3,player_4,list_challenge):
        A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the DUKE!")
                if a.cards[0]=="DUKE":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="DUKE"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1])
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0])
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
                else:
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="DUKE"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, "I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="DUKE":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the DUKE!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="DUKE"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1])
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0])
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="DUKE":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the DUKE!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="DUKE"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[0])
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        else:
            ...
#################################   CAPTAIN   #################################
    def challenge_CAPTAIN(self,board,player_1,player_2,player_3,player_4,list_challenge):
        A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
                    win_challenge=1
                    print(A+a.name,""+E+"you didn´t lie, you have the CAPTAIN!")
                if a.cards[0]=="CAPTAIN":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="CAPTAIN"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
                else:
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="CAPTAIN"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], "you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input("Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="CAPTAIN":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the CAPTAIN!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="CAPTAIN"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], "you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input("Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="CAPTAIN":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the CAPTAIN!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="CAPTAIN"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        else:
            ...
################################# AMBASSADOR  #################################  
    def challenge_AMBASSADOR(self,board,player_1,player_2,player_3,player_4,list_challenge):
        A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
        if a.vcards[0]==False and a.vcards[1]==False:
            if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
                win_challenge=1
                print(a.name,"you didn´t lie, you have the AMBASSADOR!")
                if a.cards[0]=="AMBASSADOR":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="AMBASSADOR"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input("Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
                else:
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="AMBASSADOR"
                    print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                    if list_challenge[0]==b.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                                b.vcards[0]=True
                    elif list_challenge[0]==c.name:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(list_challenge[0], ""+E+"you lose the challenge")
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[0]==True and a.vcards[1]==False:
            if a.cards[1]=="AMBASSADOR":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the AMBASSADOR!")
                a.cards[1]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="AMBASSADOR"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[1]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], "you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        elif a.vcards[1]==True and a.vcards[0]==False:
            if a.cards[0]=="AMBASSADOR":
                win_challenge=1
                print(A+a.name,""+E+"you didn´t lie, you have the AMBASSADOR!")
                a.cards[0]=board.cards[0]
                i=6
                while i!=0:
                    board.cards[i-1]=board.cards[i]
                    i-=1
                board.cards[6]="AMBASSADOR"
                print(A+a.name, ""+E+"this is your new card",A+a.cards[0]+E)
                if list_challenge[0]==b.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif list_challenge[0]==c.name:
                    print(list_challenge[0], ""+E+"you lose the challenge")
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(list_challenge[0], "you lose the challenge")
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            else: 
                print (A+a.name,""+E+"sorry, but they know that you lie :( , you lose a card")
                win_challenge=2
                if a.vcards[0]==False and a.vcards[1]==False:
                    delete=int(input(""+E+"Do you want to lose card 1 or card 2? :"))
                    if delete==1:
                        print(A+a.cards[0], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[0]=True
                    else:
                        print(A+a.cards[1], ""+E+"this is the card that", A+a.name, ""+E+"just lost")
                        a.vcards[1]=True
                else:
                    if a.vcards[0]==True:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[1]+E)
                        a.vcards[1]=True
                    else:
                        print(A+a.name,""+E+"I´m sorry but you lose, your last card was", A+a.cards[0]+E)
                        a.vcards[0]=True
        else:
            ...
#################################  PLAY GAME  #################################    
    def play(self,board,player_1,player_2,player_3,player_4):
        
        n_players = board.n_players
        if n_players==4:
            A,B,C,D,E,a,b,c,d = cond(board,player_1,player_2,player_3,player_4)
            print(A+a.name)
            if a.coins>=10:
                while True:
                    try:
                        p_1=int(input(""+E+"I´m sorry but you need to use your coins... yo have to use the Coup(=5) or the Murderer(=2) wich one do you choose?"))
                        if (p_1 == 5) or (p_1 == 2):
                            break
                        else:
                            print("Pls, type ´5´ or ´2´ number")
                    except:
                        print("Pls, type ´5´ or ´2´ number")

                if p_1== 5:
                    print (A+a.name, ""+E+"choose to play Coup")
                else:
                    print (A+a.name, ""+E+"choose to play Murderer")
            else:
                p_1=int(input (""+E+"wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid :"))
                if p_1==1:
                    print (A+a.name, ""+E+"choose to play Duke")  
                elif p_1==2:
                    if a.coins>=3:
                        print (A+a.name, ""+E+"choose to play Murderer") 
                    else:
                        while True:
                            try:
                                print(""+E+"I´m sorry but you dont have enought coins... pls, chose other number")
                                p_1=int(input(""+E+"wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid :"))
                                if p_1 != 2 and p_1 != 5:
                                    break
                                else:
                                    print(""+E+"Pls,don´t type ´5´ or ´2´ number")
                            except:
                                print(""+E+"Pls,don´t type ´5´ or ´2´ number")
                elif p_1==3:
                    print(A+a.name ,""+E+"choose to play Captain")
                elif p_1==4:
                    print(A+a.name, ""+E+"choose to play Ambassador")
                elif p_1==5:
                    if a.coins>=7:
                        print (A+a.name, ""+E+"choose to play Coup")
                    else:
                        while True:
                            try:
                                print(""+E+"I´m sorry but you dont have enought coins... pls, chose other number")
                                p_1=int(input(""+E+"wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid :"))
                                if p_1 != 5:
                                    break
                                else:
                                    print(""+E+"Pls,don´t type ´5´")
                            except:
                                print(""+E+"Pls,don´t type ´5´")
                elif p_1==6:
                    print (A+a.name, ""+E+"choose to play Income")
                else:
                    print(A+a.name ,""+E+"choose to play foreign aid")
            if p_1==2 or p_1==3:
                print (A+a.name)
                attack=input (""+E+"wich player do you whant to attack? :")
                print (attack)
            else:
                ...
            if p_1==1 or p_1==2 or p_1==3 or p_1==4:
                print(B+b.name)
                p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                print(C+c.name)
                p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                print(D+d.name)
                p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                list_challenge=[]
                if p_2==1 and p_3==1 and p_4==1:
                    list_challenge.append(b.name)
                    list_challenge.append(c.name)
                    list_challenge.append(d.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_2==1 and p_3==1:
                    list_challenge.append(b.name)
                    list_challenge.append(c.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_2==1 and p_4==1:
                    list_challenge.append(b.name)
                    list_challenge.append(d.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_3==1 and p_4==1:
                    list_challenge.append(c.name)
                    list_challenge.append(d.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_2==1:
                    list_challenge.append(b.name)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_3==1:
                    list_challenge.append(d.name)
                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                elif p_4==1:
                    list_challenge.append(d.name)
                    print(D+d.name, ""+E+"you do the challenge, good luck")
                    if p_1==1:
                        self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==2:
                        self.challenge_MURDERER(board,player_1,player_2,player_3,player_4,list_challenge)
                    elif p_1==3:
                        self.challenge_CAPTAIN(board,player_1,player_2,player_3,player_4,list_challenge)
                    else:
                        self.challenge_AMBASSADOR(board,player_1,player_2,player_3,player_4,list_challenge)
                else:
                    print(""+E+"no challenge")
            elif p_1==5:
                a.coins-=7
                k_o=input(""+E+"wich player lose 1 influence :")
                if k_o==b.name:
                    print(B+b.name, ""+E+"I´m sorry but you lose a card")
                    if b.vcards[0]==False and b.vcards[1]==False:
                        print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                            b.vcards[0]=True
                        else:
                            print(b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                            b.vcards[1]=True
                    else:
                        if b.vcards[0]==True:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1]+E)
                            b.vcards[1]=True
                        else:
                            print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0]+E)
                            b.vcards[0]=True
                elif k_o==c.name:
                    print(C+c.name, ""+E+"I´m sorry but you lose a card")
                    if c.vcards[0]==False and c.vcards[1]==False:
                        print(C+c.cards[0].c.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                            c.vcards[0]=True
                        else:
                            print(c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                            c.vcards[1]=True
                    else:
                        if c.vcards[0]==True:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                            c.vcards[1]=True
                        else:
                            print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                            c.vcards[0]=True
                else:
                    print(D+d.name, ""+E+"I´m sorry but you lose a card")
                    if d.vcards[0]==False and d.vcards[1]==False:
                        print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                        delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                        if delete==1:
                            print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                            d.vcards[0]=True
                        else:
                            print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                            d.vcards[1]=True
                    else:
                        if d.vcards[0]==True:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                            d.vcards[1]=True
                        else:
                            print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                            d.vcards[0]=True
            elif p_1==6:
                a.coins +=1
            else:
                print(""+E+"If someone wants to do a contra attack you will need the Duke")
                print(B+b.name)
                ask2=int(input(""+E+"Do you want to contra attack? 1= yes 2= no :"))
                print(C+c.name)
                ask3=int(input(""+E+"Do you want to contra attack? 1= yes 2= no :"))
                print(D+d.name)
                ask4=int(input(""+E+"Do you want to contra attack? 1= yes 2= no :"))
                if ask2==2 and ask3==2 and ask4==2:
                    a.coins+=2
                else:
                    ####### CORREGIR #####
                    if ask2==1:
                        list_challenge=[]
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                        else:
                            print(""+E+"we have a challenge!")
                            if p_2==1 and p_3==1 and p_4==1:
                                e = a
                                a = b
                                b = e
                                list_challenge.append(b.name)
                                list_challenge.append(c.name)
                                list_challenge.append(d.name)
                                random.shuffle(list_challenge)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    e = a
                                    a = b
                                    b = e
                                else: 
                                    e = a
                                    a = b
                                    b = e
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_2==1 and p_3==1:
                                list_challenge.append(b.name)
                                list_challenge.append(c.name)
                                random.shuffle(list_challenge)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_2==1 and p_4==1:
                                list_challenge.append(b.name)
                                list_challenge.append(d.name)
                                random.shuffle(list_challenge)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_3==1 and p_4==1:
                                list_challenge.append(c.name)
                                list_challenge.append(d.name)
                                random.shuffle(list_challenge)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_2==1:
                                e = a
                                a = b
                                b = e
                                list_challenge.append(b.name)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_3==1:
                                e = a
                                a = b
                                b = e
                                list_challenge.append(d.name)
                                print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")
                            elif p_4==1:
                                e = a
                                a = b
                                b = e
                                list_challenge.append(d)
                                print(D+d.name, ""+E+"you do the challenge, good luck")
                                self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                if win_challenge==1:
                                    print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                else: 
                                    a.coins+=2 
                                    print( A+a.name, ""+E+" you can have the two coins")       
                    elif ask3==1:
                        ###### CORREGIR ####### 
                        e = a
                        a = c
                        c = e
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can have the two coins")
                        else:
                            print(""+E+"we have a challenge!")
                    elif ask4==1: 
                        e = a
                        a = c
                        c = e
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can have the two coins")
                        else:
                            print(""+E+"we have a challenge!")
                            if p_2==2 and p_3==2 and p_4==2:
                                print (""+E+"I´m sorry", A+a.name, ""+E+"but you can have the two coins")
                            else:
                                print(""+E+"we have a challenge!")
                                if p_2==1 and p_3==1 and p_4==1:
                                    list_challenge.append(b.name)
                                    list_challenge.append(c.name)
                                    list_challenge.append(d.name)
                                    random.shuffle(list_challenge)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")

                                elif p_2==1 and p_3==1:
                                    list_challenge.append(b.name)
                                    list_challenge.append(c.name)
                                    random.shuffle(list_challenge)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                                elif p_2==1 and p_4==1:
                                    list_challenge.append(b.name)
                                    list_challenge.append(d.name)
                                    random.shuffle(list_challenge)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                                elif p_3==1 and p_4==1:
                                    list_challenge.append(c.name)
                                    list_challenge.append(d.name)
                                    random.shuffle(list_challenge)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                                elif p_2==1:
                                    list_challenge.append(b.name)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                                elif p_3==1:
                                    list_challenge.append(d.name)
                                    print(list_challenge[0], ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                                elif p_4==1:
                                    list_challenge.append(d.name)
                                    print(D+d.name, ""+E+"you do the challenge, good luck")
                                    self.challenge_DUKE(board,player_1,player_2,player_3,player_4,list_challenge)
                                    if win_challenge==1:
                                        print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t have the two coins")
                                    else: 
                                        a.coins+=2 
                                        print( A+a.name, ""+E+" you can have the two coins")
                    else: #si se hacen los challenge y gana el challenge player 1
                        a.coins+=2
            if p_1==2: 
                a.coins -=3
                print(""+E+"To defense this attack you will need the Countess")
                print(attack)
                ask=int(input(""+E+"Do you whant to defense? 1= yes 2= no :"))
                if ask==2:
                    if attack==b.name:
                        print(B+b.name, ""+E+"I´m sorry but you lose a card")
                        if b.vcards[0]==False and b.vcards[1]==False:
                            print(B+b.cards[0],b.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(B+b.cards[0], ""+E+"this is the card that", B+b.name,""+E+"just lost")
                                b.vcards[0]=True
                            else:
                                print(B+b.cards[1], ""+E+"this is the card that", B+b.name, ""+E+"just lost")
                                b.vcards[1]=True
                        else:
                            if b.vcards[0]==True:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[1])
                                b.vcards[1]=True
                            else:
                                print(B+b.name,""+E+"I´m sorry but you lose, your last card was", B+b.cards[0])
                                b.vcards[0]=True
                    elif attack==c.name:
                        print(C+c.name, ""+E+"I´m sorry but you lose a card")
                        if c.vcards[0]==False and c.vcards[1]==False:
                            print(C+c.cards[0],c.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(C+c.cards[0], ""+E+"this is the card that", C+c.name,""+E+"just lost")
                                c.vcards[0]=True
                            else:
                                print(C+c.cards[1], ""+E+"this is the card that", C+c.name, ""+E+"just lost")
                                c.vcards[1]=True
                        else:
                            if c.vcards[0]==True:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[1]+E)
                                c.vcards[1]=True
                            else:
                                print(C+c.name,""+E+"I´m sorry but you lose, your last card was", C+c.cards[0]+E)
                                c.vcards[0]=True
                    else:
                        print(D+d.name, ""+E+"I´m sorry but you lose a card")
                        if d.vcards[0]==False and d.vcards[1]==False:
                            print(D+d.cards[0],d.cards[1], ""+E+"this is(are) you(r) card(s)")
                            delete=int(input(""+E+"Do you whant to lose card 1 or card 2? :"))
                            if delete==1:
                                print(D+d.cards[0], ""+E+"this is the card that", D+d.name,""+E+"just lost")
                                d.vcards[0]=True
                            else:
                                print(D+d.cards[1], ""+E+"this is the card that", D+d.name, ""+E+"just lost")
                                d.vcards[1]=True
                        else:
                            if d.vcards[0]==True:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[1]+E)
                                d.vcards[1]=True
                            else:
                                print(D+d.name,""+E+"I´m sorry but you lose, your last card was", D+d.cards[0]+E)
                                d.vcards[0]=True
                else:
                    if attack==b.name:
                        print(B+b.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack")
                        else:
                            print(""+E+"we have a challenge!")
                    elif attack==c.name:
                        print(C+c.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack")
                        else:
                            print(""+E+"we have a challenge!")
                    else:
                        print(D+d.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack ")
                        else:
                            print(""+E+"we have a challenge!")
            elif p_1==3:
                print (""+E+"To defense this attack you will need the ambassador or the captain")
                print (attack)                
                ask=int(input(""+E+"Do you whant to defense? 1= yes 2= no :"))
                if ask==2:
                    if attack==b.name:
                        if b.coins>=2:
                            b.coins-=2
                            a.coins+=2
                            print(""+E+"sorry",B+b.name,""+E+"but",A+a.name,""+E+"take 2 of your coins")
                        elif b.coins==1:
                            b.coins-=1
                            a.coins+=1
                            print(""+E+"sorry",B+b.name,""+E+"but",A+a.name,""+E+"take the last coin you have")
                        else:
                            print(A+a.name,""+E+"bad call...", B+b.name,""+E+"don´t have coins...")
                    elif attack==c.name:
                        if c.coins>=2:
                            c.coins-=2
                            a.coins+=2
                            print(""+E+"sorry",C+c.name,""+E+"but",A+a.name,""+E+"take 2 of your coins")
                        elif c.coins==1:
                            c.coins-=1
                            a.coins+=1
                            print(""+E+"sorry",C+c.name,""+E+"but",A+a.name,""+E+"take the last coin you have")
                        else:
                            print(A+a.name,""+E+"bad call...", C+c.name,""+E+"don´t have coins...")
                    else:
                        if d.coins>=2:
                            d.coins-=2
                            a.coins+=2
                            print(""+E+"sorry",D+d.name,""+E+"but",A+a.name,""+E+"take 2 of your coins")
                        elif d.coins==1:
                            d.coins-=1
                            a.coins+=1
                            print(""+E+"sorry",D+d.name,""+E+"but",A+a.name,""+E+"take the last coin you have")
                        else:
                            print(A+a.name,""+E+"bad call...", D+d.name,""+E+"don´t have coins...")
                else:
                    if attack==b.name:
                        print(B+b.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack")
                        else:
                            print(""+E+"we have a challenge!")
                    elif attack==c.name:
                        print(C+c.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(D+d.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack")
                        else:
                            print(""+E+"we have a challenge!")
                    else:
                        print(D+d.name,""+E+"use the defense")
                        print(A+a.name)
                        p_2=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(B+b.name)
                        p_3=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        print(C+c.name)
                        p_4=int(input(""+E+"Do you whant to do a challenge; 1 yes 2 no :"))
                        if p_2==2 and p_3==2 and p_4==2:
                            print (""+E+"I´m sorry", A+a.name, ""+E+"but you can´t do your attack ")
                        else:
                            print(""+E+"we have a challenge!") 
            elif p_1==4:
                if p_2==2 and p_3==2 and p_4==2:
                    print(A+a.name,""+E+"you can choose 2 cards between your own cards and 2 of the desk")
                    if a.vcards[0]==False and a.vcards[1]==False:
                        print(""+E+"this are the cards, you have to choose 1 each time")
                        print(A+a.cards[0],""+E+"=1",A+a.cards[1],""+E+"=2",board.cards[0],"=3",board.cards[1],"=4")
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
                        print(A+a.name, ""+E+"this are your cards after your choice:")
                        print(A+a.cards)
                    else:
                        print(A+a.name,""+E+"you can choose 1 cards between your own card and 2 of the desk")
                        print(""+E+"this are the cards, you have to choose 1")
                        if a.vcards[0]==True:
                            print(A+a.cards[1],""+E+"=1",board.cards[0],"=3",board.cards[1],"=4")
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
                            print(A+a.cards[1],""+E+"=1",board.cards[0],"=3",board.cards[1],"=4")
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
                if p_2==2 and p_3==2 and p_4==2:
                    print(A+a.name,""+E+"good for you! you earn 3 coins")
                    a.coins +=3
                else:
                    ...
            else: 
                ...
