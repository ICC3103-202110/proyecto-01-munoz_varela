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