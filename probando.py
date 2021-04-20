
########################################################################################################33
    def challenge_b1(self,board,b,a):
        if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==b.name:
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
                if a.cards[0]=="DUKE":
                    board.cards[6]="DUKE"
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
        
                else:
                    a.cards[1]=board.cards[0]
                    board.cards[6]="DUKE"
                    print(a.name, "this is your new card",board.cards[0])
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

    def challenge_2(self,board,a,b,c,d):
        if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==b.name:
                print(b.name, "I´m sorry but you lose the game :(")
                b.vcards[0]=True
                b.vcards[1]=True
                if a.cards[0]=="MURDERER":
                    a.cards[0]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(a.name, "this is your new card",a.cards[0])
                else:
                    a.cards[1]=board.cards[0]
                    i=6
                    while i!=0:
                        board.cards[i-1]=board.cards[i]
                        i-=1
                    board.cards[6]="MURDERER"
                    print(a.name, "this is your new card",a.cards[1])
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
    def challenge_b3(self,board,b,a):
        if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==b.name:
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
                if a.cards[0]=="CAPTAIN":
                    board.cards[6]="CAPTAIN"
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    board.cards[6]="CAPTAIN"
                    a.cards[1]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[0])
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
    def challenge_b4(self,board,b,a):
        if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==b.name:
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
                if a.cards[0]=="AMBASSADOR":
                    board.cards[6]="AMBASSADOR"
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[1]=board.cards[0]
                    board.cards[6]="AMBASSADOR"
                    print(a.name, "this is your new card",board.cards[0])
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
    def challenge_c1(self,board,c,a):
        if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==c.name:
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
                if a.cards[0]=="DUKE":
                    board.cards[6]="DUKE"
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[1]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
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
    def challenge_c2(self,board,c,a):
        if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==c.name:
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
                if a.cards[0]=="MURDERER":
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[0]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[1])
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
    def challenge_c3(self,board,c,a):
        if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==c.name:
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
                if a.cards[0]=="CAPTAIN":
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[0]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[1])
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
    def challenge_c4(self,board,c,a):
        if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==c.name:
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
    def challenge_d1(self,board,d,a):
        if a.cards[0]=="DUKE" or a.cards[1]=="DUKE":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==d.name:
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
    def challenge_d2(self,board,d,a):
        if a.cards[0]=="MURDERER" or a.cards[1]=="MURDERER":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==d.name:
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
                if a.cards[0]=="MURDERER":
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[0]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[1])
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
    def challenge_d3(self,board,d,a):
        if a.cards[0]=="CAPTAIN" or a.cards[1]=="CAPTAIN":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==d.name:
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
                if a.cards[0]=="CAPTAIN":
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[0]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[1])
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
    def challenge_d4(self,board,d,a):
        if a.cards[0]=="AMBASSADOR" or a.cards[1]=="AMBASSADOR":
            (list_challenge[0], "you lose the challenge")
            if list_challenge[0]==d.name:
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
                if a.cards[0]=="AMBASSADOR":
                    a.cards[0]=board.cards[0]
                    print(a.name, "this is your new card",board.cards[0])
                else:
                    a.cards[0]=board.cards[1]
                    print(a.name, "this is your new card",board.cards[1])
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