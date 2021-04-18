import random
class Influences:
    def __init__(self):
        ...
    
    def play(self,board,player_1,player_2,player_3,player_4):
        n_players = board.n_players
        turn = board.turn
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

        if n_players==4:
<<<<<<< HEAD
            if turn==1:
                print(player_1.name)
                p_1=int(input ("wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid :"))
                if p_1==1:
                    print (player_1.name, "choose to play Duke")  
                elif p_1==2:
                    print (player_1.name, "choose to play Murderer") 
                elif p_1==3:
                    print(player_1.name ,"choose to play Captain")
                elif p_1==4:
                    print(player_1.name, "choose to play Ambassador")
                elif p_1==5:
                    print (player_1.name, "choose to play Coup")
                elif p_1==6:
                    print (player_1.name, "choose to play Income")
                else:
                    print(player_1.name ,"choose to play foreign aid")
                if p_1==2 or p_1==3:
                    print (player_1.name)
                    attack=input ("wich player do you whant to attack? :")
                    print (attack)
                else:
                    ...
                if p_1==1 or p_1==2 or p_1==3 or p_1==4:
                    print(player_2.name)
                    p_2=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(player_3.name)
                    p_3=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    print(player_4.name)
                    p_4=int(input("Do you whant to do a challenge; 1 yes 2 no :"))
                    list_challenge=[]
                    if p_2==1 and p_3==1 and p_4==1:
                        list_challenge.append(player_2.name)
                        list_challenge.append(player_3.name)
                        list_challenge.append(player_4.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                        if p_1==1:
                            if player_1.cards[0]=="DUKE" or player_1.cards[1]=="DUKE":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]=player_2.name:
                                    print(player_2.name, "I´m sorry but you lose a card")
                                    print(player_2.cards, "this is(are) you(r) card(s)")
                                    if len(player_2.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_2.cards[0], "this is the card that", player_2.name,"just lost")
                                            player_2.vcards[0]=True
                                        else:
                                            print(player_2.cards[1], "this is the card that", player_2.name, "just lost")
                                            player_2.vcards[1]=True
                                    else:
                                        if player_2.vcards[0]=True:
                                            print(player_2.name,"I´m sorry but you lose, your last card was", player_2.cards[1])
                                            player_2.vcards[1]=True
                                        else:
                                            print(player_2.name,"I´m sorry but you lose, your last card was", player_2.cards[0])
                                            player_2.vcards[0]=True
                                elif list_challenge[0]=player_3.name:
                                    print(player_3.name, "I´m sorry but you lose a card")
                                    print(player_3.cards, "this is(are) you(r) card(s)")
                                    if len(player_3.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_3.cards[0], "this is the card that", player_3.name, "just lost")
                                            player_3.vcards[0]=True
                                        else:
                                            print(player_3.cards[1], "this is the card that", player_3.name, "just lost")
                                            player_3.vcards[1]=True
                                    else:
                                        if player_3.vcards[0]=True:
                                            print(player_3.name,"I´m sorry but you lose, your last card was", player_3.cards[1])
                                            player_3.vcards[1]=True
                                        else:
                                            print(player_3.name,"I´m sorry but you lose, your last card was", player_3.cards[0])
                                            player_3.vcards[0]=True
                                else: 
                                    print(player_4.name, "I´m sorry but you lose a card")
                                    print(player_4.cards, "this is(are) you(r) card(s)")
                                    if len(player_4.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_4.cards[0], "this is the card that", player_4.name, "just lost")
                                            player_4.vcards[0]=True
                                        else:
                                            print(player_4.cards[1], "this is the card that", player_4.name, "just lost")
                                            player_4.vcards[1]=True
                                    else:
                                        if player_4.vcards[0]=True:
                                            print(player_4.name,"I´m sorry but you lose, your last card was", player_4.cards[1])
                                            player_4.vcards[1]=True
                                        else:
                                            print(player_4.name,"I´m sorry but you lose, your last card was", player_4.cards[0])
                                            player_4.vcards[0]=True
                                if players_1.cards[0]=="DUKE":
                                    player_1.cards[0]=board.cards[0]
                                    print(player_1.name, "this is your new card",board.cards[0])
                                else:
                                    player_1.cards[0]=board.cards[1]
                                    print(player_1.name, "this is your new card",board.cards[1])
                            else: 
                                print (player_1.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(player_1.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(player_1.cards[0], "this is the card that", player_1.name, "just lost")
                                        player_1.vcards[0]=True
                                    else:
                                        print(player_1.cards[1], "this is the card that", player_1.name, "just lost")
                                        player_1.vcards[1]=True
                                else:
                                    if player_1.vcards[0]=True:
                                        print(player_1.name,"I´m sorry but you lose, your last card was", player_1.cards[1])
                                        player_1.vcards[1]=True
                                    else:
                                        print(player_1.name,"I´m sorry but you lose, your last card was", player_1.cards[0])
                                        player_1.vcards[0]=True
                        elif p_1==2:
                            if player_1.cards[0]=="MURDERER" or player_1.cards[1]=="MURDERER":
                                print(list_challenge[0], "you lose the challenge")
                                if list_challenge[0]=player_2.name:
                                    print(player_2.name, "I´m sorry but you lose a card")
                                    print(player_2.cards, "this is(are) you(r) card(s)")
                                    if len(player_2.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_2.cards[0], "this is the card that", player_2.name,"just lost")
                                            player_2.vcards[0]=True
                                        else:
                                            print(player_2.cards[1], "this is the card that", player_2.name, "just lost")
                                            player_2.vcards[1]=True
                                    else:
                                        if player_2.vcards[0]=True:
                                            print(player_2.name,"I´m sorry but you lose, your last card was", player_2.cards[1])
                                            player_2.vcards[1]=True
                                        else:
                                            print(player_2.name,"I´m sorry but you lose, your last card was", player_2.cards[0])
                                            player_2.vcards[0]=True
                                elif list_challenge[0]=player_3.name:
                                    print(player_3.name, "I´m sorry but you lose a card")
                                    print(player_3.cards, "this is(are) you(r) card(s)")
                                    if len(player_3.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_3.cards[0], "this is the card that", player_3.name, "just lost")
                                            player_3.vcards[0]=True
                                        else:
                                            print(player_3.cards[1], "this is the card that", player_3.name, "just lost")
                                            player_3.vcards[1]=True
                                    else:
                                        if player_3.vcards[0]=True:
                                            print(player_3.name,"I´m sorry but you lose, your last card was", player_3.cards[1])
                                            player_3.vcards[1]=True
                                        else:
                                            print(player_3.name,"I´m sorry but you lose, your last card was", player_3.cards[0])
                                            player_3.vcards[0]=True
                                else: 
                                    print(player_4.name, "I´m sorry but you lose a card")
                                    print(player_4.cards, "this is(are) you(r) card(s)")
                                    if len(player_4.cards==2):
                                        delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                        if delete==1:
                                            print(player_4.cards[0], "this is the card that", player_4.name, "just lost")
                                            player_4.vcards[0]=True
                                        else:
                                            print(player_4.cards[1], "this is the card that", player_4.name, "just lost")
                                            player_4.vcards[1]=True
                                    else:
                                        if player_4.vcards[0]=True:
                                            print(player_4.name,"I´m sorry but you lose, your last card was", player_4.cards[1])
                                            player_4.vcards[1]=True
                                        else:
                                            print(player_4.name,"I´m sorry but you lose, your last card was", player_4.cards[0])
                                            player_4.vcards[0]=True
                                if players_1.cards[0]=="DUKE":
                                    player_1.cards[0]=board.cards[0]
                                    print(player_1.name, "this is your new card",board.cards[0])
                                else:
                                    player_1.cards[0]=board.cards[1]
                                    print(player_1.name, "this is your new card",board.cards[1])
                            else: 
                                print (player_1.name,"sorry, but they know that you lie :( , you lose a card")
                                if len(player_1.cards==2):
                                    delete=int(input("Do you whant to lose card 1 or card 2? :"))
                                    if delete==1:
                                        print(player_1.cards[0], "this is the card that", player_1.name, "just lost")
                                        player_1.vcards[0]=True
                                    else:
                                        print(player_1.cards[1], "this is the card that", player_1.name, "just lost")
                                        player_1.vcards[1]=True
                                else:
                                    if player_1.vcards[0]=True:
                                        print(player_1.name,"I´m sorry but you lose, your last card was", player_1.cards[1])
                                        player_1.vcards[1]=True
                                    else:
                                        print(player_1.name,"I´m sorry but you lose, your last card was", player_1.cards[0])
                                        player_1.vcards[0]=True    

                
                    elif p_2==1 and p_3==1:
                        list_challenge.append(player_2.name)
                        list_challenge.append(player_3.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                    elif p_2==1 and p_4==1:
                        list_challenge.append(player_2.name)
                        list_challenge.append(player_4.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                    elif p_3==1 and p_4==1:
                        list_challenge.append(player_3.name)
                        list_challenge.append(player_4.name)
                        random.shuffle(list_challenge)
                        print(list_challenge[0], "you do the challenge, good luck")
                    elif p_2==1:
                        list_challenge.append(player_2.name)
                        print(player_2.name, "you do the challenge, good luck")
                    elif p_3==1:
                        list_challenge.append(player_3.name)
                        print(player_3.name, "you do the challenge, good luck")
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
=======
            print(a.name)
            p_1=int(input ("wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid"))
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
                attack=input ("wich player do you whant to attack?")
                print (attack)
            else:
                ...
            if p_1==1 or p_1==2 or p_1==3 or p_1==4:
                print(b.name)
                p_2=int(input("Do you whant to do a challenge; 1 yes 2 no"))
                print(c.name)
                p_3=int(input("Do you whant to do a challenge; 1 yes 2 no"))
                print(d.name)
                p_4=int(input("Do you whant to do a challenge; 1 yes 2 no"))
                #hacer que el jugador demuestre tener la carta en el challenge
                list_challenge=[]
                if p_2==1 and p_3==1 and p_4==1:
                    list_challenge.append(b.name)
                    list_challenge.append(c.name)
                    list_challenge.append(d.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], "you do the challenge, good luck")
                    if p_1==1:
                        if a.cards[0]=="DUKE" or a.card[1]=="DUKE":
                            print(list_challenge[0], "you lose the challenge")
                            if a.cards[0]=="DUKE":
                                 ...

                elif p_2==1 and p_3==1:
                    list_challenge.append(b.name)
                    list_challenge.append(c.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], "you do the challenge, good luck")
                elif p_3==1 and p_4==1:
                    list_challenge.append(c.name)
                    list_challenge.append(d.name)
                    random.shuffle(list_challenge)
                    print(list_challenge[0], "you do the challenge, good luck")
                elif p_2==1:
                    list_challenge.append(b.name)
                    print(b.name, "you do the challenge, good luck")
                elif p_3==1:
                    list_challenge.append(c.name)
                    print(c.name, "you do the challenge, good luck")
                elif p_4==1:
                    list_challenge.append(d.name)
                    print(d.name, "you do the challenge, good luck")
                else:
                    list_challenge.append("no challenge")
                    print (list_challenge)
            elif p_1==5:
                a.coins-=7
                k_o=input("wich player lose 1 influence")
                #hacer elegir al jugador atacado que carta pierde 
            elif p_1==6:
                a.coins +=1
            else:
                print("If someone whants to do a contra attack you will need the Duke")
                print(b.name)
                ask2=int(input("Do you whant to contra attack? 1= yes 2= no"))
                print(c.name)
                ask3=int(input("Do you whant to contra attack? 1= yes 2= no"))
                print(d.name)
                ask4=int(input("Do you whant to contra attack? 1= yes 2= no"))
                if ask2==2 and ask3==2 and ask4==2:
                    a.coins+=2
                else:
                    if ask2==1:
                        ...#preguntar a los jugadores si quieren challenge
                    elif ask3==1: #agregar un and que la jugada no se haya cortado
                        ...#preguntar a los jugadores si quieren challenge
                    elif ask4==1: #agregar un and que la jugada no se haya cortado
                        ...#preguntar a los jugadores si quieren challenge
                    else:
                        a.coins+=2
            if p_1==2: 
                a.coins -=3
                print("To defense this attack you will need the Countess")
                print(attack)
                ask=int(input("Do you whant to defense? 1= yes 2= no"))
                if ask==2:
                    ...#hacer elegir que carta pierde
                else:
                    ...#preguntar a los jugadores si quieren hacer un challenge 
            elif p_1==3:
                print ("To defense this attack you will need the ambassador or the captain")
                print (attack)
                ask=int(input("Do you whant to defense? 1= yes 2= no"))
                if ask==2:
                    ...#hacer un if el jugador atacado tiene menos de 2 monedas robar 1 else robar 2
                else:
                    ...#preguntar a los jugadores si quieren hacer un challenge 
            elif p_1==4:
                ...#permitir ver dos cartas del mazo y elegir con cuales se queda
            elif p_1==1:
                a.coins +=3
            else: 
                ...
>>>>>>> 48c895f40b42c1d9bb2422c6269e97bc489683a6
