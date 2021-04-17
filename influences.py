#DUKE 3 COINS FOR THE PLAYER
#MURDERER PAY 3 COINS TO KILL 1 INFLUENCE OF OTHER PLAYER, THE OTHER PLAYER CHOOSE WICH CARD HE LOSE
#MURDERER CAN BE BLOCK WITH THE COUNTESS
#CAPTAIN TAKE 2 COINS OF OTHER PLAYER (MAX)
#CAPTAIN CAN BE BLOCK BY CAPTAIN OR AMBASSADOR
#AMBASSADOR CAN CHANGE HIS CARDS, MUST TAKE 2 CARDS FROM DE DESK
#AND CHOOSE 2 BETWEEN THE CRADS THAT ALREADY HAVE AN THE ONES HE TAKES FROM THE DESK, 2 OF THIS CARDS KEEP THE PLAYER
# AND THE OTHER TWO RETURN TO THE DESK
#COUNTESS

class Duke (self,x,y,w,z):
    #preguntar a los jugadores si alguno quiere desafiar esta acción, en caso de que tenga la carta quien lo desafio pierde una carta 
    #en caso contrario el jugador que hizo la acción pierde una carta
    #si dos o mas jugadores desafían se elige al azar quien es el desafiante
    #si el jugador en turno gana el desafio debe cambiar su carta por una del mazo
    #agregar 3 monedas al jugador que juegue la carta
class Murderer (self,x,y,w,z):
    #IMPORTANTE#
    #Si el jugador atacado decide desafiar al jugador en turno y este ultimo gana el atacado pierde sus dos cartas
    #Si el jugador atacado se defiende y es desafiado y no posee la carta pierde las dos cartas 
    #quitar 3 monedas al jugador 
    #elegir a que jugador quiere atacar
    kill=input("enter the name of the player you want to attack")
    #preguntar a los jugadores si alguno quiere desafiar esta acción, en caso de que tenga la carta quien lo desafio pierde una carta 
    #en caso contrario el jugador que hizo la acción pierde una carta
    #si dos o mas jugadores desafían se elige al azar quien es el desafiante
    #si el jugador en turno gana el desafio debe cambiar su carta por una del mazo
    #preguntar al jugador atacado si quiere contra atacar y darle a entender que solo se puede con la carta countess
    #si no decide contra atacar el jugador debe dar vuelta una de sus cartas 
    #si contra ataca y gana se pasa al siguiente jugador 
class Captain (self,x,y,w,z):
    #preguntar a los jugadores si alguno quiere desafiar esta acción, en caso de que tenga la carta quien lo desafio pierde una carta 
    #en caso contrario el jugador que hizo la acción pierde una carta
    #si dos o mas jugadores desafían se elige al azar quien es el desafiante
    #si el jugador en turno gana el desafio debe cambiar su carta por una del mazo
    #elegir a que jugador le quita 2 monedas (si posee 1 le quita solo 1)
    steal=input("enter the name of the player you want to steal coins")
    #puede ser bloqueado si el jugador tiene captain o ambassador 
class Ambassador (self,x,y,w,z):
    #preguntar a los jugadores si alguno quiere desafiar esta acción, en caso de que tenga la carta quien lo desafio pierde una carta 
    #en caso contrario el jugador que hizo la acción pierde una carta
    #si dos o mas jugadores desafían se elige al azar quien es el desafiante
    #si el jugador en turno gana el desafio debe cambiar su carta por una del mazo
    #mostrarle 2 cartas del mazo
    #darle a elegir al jugador con que 2 cartas se quiere quedar y devolver las otras dos al mazo
class Coup (Self,x,y):
    #debe pagar 7 monedas
    Coup=input ("enter the name of the player that you want to attack")
    #quitar una carta al jugador afectado    