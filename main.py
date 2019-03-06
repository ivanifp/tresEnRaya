from utils import numJugadores,getFicha,colocaFicha,imprimirTablero,tableroLibre,victoria
#me creo mi tablero con nueve posiciones
tablero = [' ']*9

numJu = numJugadores()

fichaj1,fichaj2 = getFicha()



while tableroLibre(tablero) or victoria(tablero,fichaj1)== False or victoria(tablero,fichaj2)== False:

    imprimirTablero(tablero)

    pos = int(input("Diga movimiento jugador Uno"+fichaj1))

    colocaFicha(tablero,pos,fichaj1)
    imprimirTablero(tablero)

    pos2 = int(input("Diga movimiento jugador Dos"+fichaj2))

    colocaFicha(tablero,pos2,fichaj2)
    imprimirTablero(tablero)

#fin tableroLibre
