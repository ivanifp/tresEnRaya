
def numJugadores():
    num = int(input('Cuantos Jugadores, 1 ó 2'))
    while num !=1 and num !=2:
        print('error, numero de jugadores')
        num = int(input('Cuantos Jugadores, 1 ó 2'))

    return num

#fin numJugadores

def getFicha():
    ficha = input('el jugador Uno va a Jugar con X ó O?').upper()
    while ficha !='X' and ficha !='O':
        print('error, ficha no valida')
        ficha = input('el jugador Uno va a Jugar con X ó O?').upper()

    if ficha=='X':
        return ['X','O']
    else:
        return ['O','X']

#fin getSimbolo

def jugadaValida(tablero, pos):
#devuelvo true o false
    if tablero[pos-1] == " ":
        return True
    else:
        return  False

#fin jugadaValida

def victoria(tablero,ficha):
    #devuelvo true o false
    #compruebo las posiciones en el tablero
    if ((tablero[0] ==ficha and tablero[1]==ficha and tablero[2] == ficha)or(tablero[3]==ficha and tablero[4]==ficha and tablero[5] == ficha)or (tablero[6]==ficha and tablero[7]==ficha and tablero[8] == ficha)or(tablero[0]==ficha and tablero[3]==ficha and tablero[6] == ficha)or(tablero[1]==ficha and tablero[4] == ficha and tablero[7] == ficha)or (tablero[2]== ficha and tablero[5]== ficha and tablero[8] == ficha)or(tablero[0]== ficha and tablero[4]== ficha and tablero[8] == ficha)or(tablero[2]== ficha and tablero[4]== ficha and tablero[6] == ficha)):
        return True
    else:
        return False
#fin victoria

def colocaFicha(tablero,pos,ficha):

    if jugadaValida(tablero,pos):
        #fijo valor en tablero
        tablero[pos-1] = ficha
        vic = victoria(tablero,ficha)
        if vic:
            print('Has ganado la partida el jugador con la ficha:',ficha)
            
    else:
        return print('#### movimiento no valido, pierdes turno...')

#fin colocaFicha

def imprimirTablero(tablero):
    print('   |   |')
    print(' ' + tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
    print('   |   |')
    print('- - - - - -/ ')
    print('   |   |')
    print(' ' + tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('   |   |')
    print('- - - - - - /')
    print('   |   |')
    print(' ' + tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('   |   |')
    print('******************************************************')

#fin imprimirTablero

def tableroLibre(tablero):

    if (tablero[0] == " " or tablero[1]== " " or tablero[2]== " " or tablero[3]== " " or tablero[4]== " " or tablero[5]== " " or tablero[6]== " " or tablero[7]== " " or tablero[8] == " "):
        return True
    else:
        return False

#fin tableroLibre
