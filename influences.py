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
