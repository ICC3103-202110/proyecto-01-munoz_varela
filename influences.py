from main import Board
if n_players==4:
    class influences (self,player_1,player_2,player_3,player_4):
        if Board.turn==1:
            print(player_1.name)
            p_1=int(input ("wich card do you whant to play; 1=Duke, 2=Murderer, 3=Captain, 4=Ambassador, 5=Coup, 6=Income, 7=Foreing aid")
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
                attack=input ("wich player do you whant to attack?")
                print (attack)
            elif p_1==4:
                #permitir ver dos cartas del mazo y elegir con cuales se queda
            elif p_1==1:
                player_1.coins +=3 
            else:
                continue
            if p_1==1 or p_1==2 or p_1==3 or p_1==4:
                print(player_2.name)
                p_2=int(input("Do you whant to do a challenge; 1 yes 2 no")
                print(player_3.name)
                p_3=int(input("Do you whant to do a challenge; 1 yes 2 no")
                print(player_4.name)
                p_4=int(input("Do you whant to do a challenge; 1 yes 2 no")
                #hacer random con los que decidieron el challenge y si no hay listo

            elif p_1==5:
                player_1.coins-=7
                k.o=input("wich player lose 1 influence")
                #hacer elegir al jugador atacado que carta pierde 
            elif p_1==6:
                player_1.coins +=1
            else:
                print("If someone whants to do a contra attack you will need the Duke")
                print(player_2.name)
                ask2=int(input("Do you whant to contra attack? 1= yes 2= no"))
                print(player_3.name)
                ask3=int(input("Do you whant to contra attack? 1= yes 2= no"))
                print(player_3.name)
                ask4=int(input("Do you whant to contra attack? 1= yes 2= no"))
                if ask2==2 and ask3==2 and ask4==2:
                    player_1.coins+=2
                else:
                    if ask2==1:
                        #preguntar a los jugadores si quieren challenge
                    elif ask3==1: #agregar un and que la jugada no se haya cortado
                        #preguntar a los jugadores si quieren challenge
                    elif ask4==1 #agregar un and que la jugada no se haya cortado
                        #preguntar a los jugadores si quieren challenge
                    else:
                        player_1.coins+=2
             if p_1==2: 
                player_1.coins -=3
                print("To defense this attack you will need the Countess")
                print(attack)
                ask=int(input("Do you whant to defense? 1= yes 2= no"))
                if ask==2:
                    #hacer elegir que carta pierde
                else:
                    #preguntar a los jugadores si quieren hacer un challenge 
            if p_1==3:
                print ("To defense this attack you will need the ambassador or the captain")
                print (attack)
            ask=int(input("Do you whant to defense? 1= yes 2= no"))
                if ask==2:
                    #hacer un if el jugador atacado tiene menos de 2 monedas robar 1 else robar 2
                else:
                    #preguntar a los jugadores si quieren hacer un challenge 
