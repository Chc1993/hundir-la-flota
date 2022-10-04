#importar librerias que se van a utilizar en el proceso
import numpy as np
import random

#Variables constantes del juego que serán utilizadas para el diseño de programación del juego
agua = "~"
barco = 'O'
barco_tocado = "@"
disparo_fallido = 'X'
#Diccionario para crear los barcos diferenciado por número de barcos y su tamaño
barcos = {"Barco de 1 eslora": (4, 1), "Barco de 2 esloras" : (3, 2), "Barco de 3 esloras": (2, 3), "Barco de 4 esloras" : (1, 4)}

#definición d las clases
class barco:
    '''
    Definición de una clase barco que estará definida por el nombre, tipo de barco y las coordenadas donde estará situado
    '''
    def __init__(self, nombre_barco, tipo_barco):
        self.nombre_barco = nombre_barco
        self.len = barcos[tipo_barco][1]
        self.coordenadas = []
class jugador1:
    '''
    Definición de una clase jugador que diferenciará que tipo de jugador es: un humano o una máquina
    '''
    def __init__(self, tipo):
        self.tipo = tipo

class tablero:
    '''
    Definición de una clase cuya función tablero va a desarrollar
    un tablero 10x10 rellenado con la variable agua
    '''
    def __init__(self, medida):#esto creo que no sirve para nada, revisar
        self.medida = (10, 10)
    def tablero():
        return np.full((10, 10), agua)

        
#Metodos
def findeljuego(tablero1: tablero, tablero2: tablero): #función para declarar cuándo el juego ha terminado(es decir, si hay barcos en el tablero del jugador humano, significa que ha ganado la partida, si no es que ha ganado la máquina)
    if barco in tablero1:
        print("Jugador humano ha ganado! Enhorabuena")
        exit() 
    else:
        print("La máquina ha ganado! Juega otra partida")
        exit() 
        
def menu():
    print('''Opciones de juego:
          1. Dispara
          2. Mirar tablero de jugador 1
          3. Mirar tablero del contrario
          4. Salir''')


def disparo(jugador1: jugador1, tablero: tablero):
    if jugador1.tipo == 'Humano':
        while 1:#bucle paera comprobar que las coordenadas introducidas estan dentro del tablero
            while 1:#bucle para comprobar que el formato introducido es correcto
                try:
                    fila, col = [int(coord) for coord in input("Indica coordenadas a las que lanzar un disparo").split()]
                    break #salir del segundo bucle
                except ValueError:
                    print('Los valores introducidos no son correctos')
            if (fila < 0 or fila > 9) or (col < 0 or col > 9):
                print('Las coordenadas introducidas no son correctas')
            else:
                break #salir del primer bucle
    else: #Los disparos del contrincante son aleatorios
        fila = random.randint(0,10-1)
        col = random.randint(0,10-1)
    
    if tablero[fila, col] == barco:
        print("BARCO TOCADO")
        tablero[fila, col] = barco_tocado #Barco tocado será representado con @ en dicha fila y columna
        if barco not in tablero: #Si no hay más barcos sobre el tablero que declare el final del juego y el ganador
            findeljuego()
        #Si no, y hay barcos todavía, sigue la partida
        disparo(jugador1, tablero)
    elif tablero[fila, col] == agua: #Disparo fallido
        print("AGUA! No has tocado ningún barco")
        tablero[fila, col] = disparo_fallido
    elif tablero[fila, col] == barco_tocado or tablero[fila, col] == disparo_fallido:
        print("Ya has disparado en esta fila-columna. Por favor, elige otras coordenadas")
        disparo(jugador1, tablero)
        
def ejercito_barcos(tablero: tablero):
    ejercito_barcos = []
    for i in barcos.keys():
        for num in range(barcos[i][0]):
            barco_nuevo = barco(i + str(num), i)
            situa_barcos_tablero(barco_nuevo, tablero)
            ejercito_barcos.append(barco_nuevo)
    return ejercito_barcos

def situa_barcos_tablero(barco: barco, tablero: tablero):
    situado = False
    orientaciones = ['N', 'E', 'S', 'O']
    
    while not situado:
        fila = random.randint(0,tablero-1)
        col = random.randint(0,tablero-1)
        orientacion = random.choice(orientaciones)
        
        if tablero[fila, col] == agua:
            if orientacion == 'N':
                if fila - (barco.len -1) < 0:
                    #Si fila - (barco.len -1) es menor que 0 significa que el barco  está en el lado norte del tablero
                    continue
                else: #comporbar si el barco puede situarse
                    for celda in range(barco.len):
                        if tablero[fila-celda, col] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    #Si puede situarse, el barco se coloca y salir del bucle
                    if situado == True:
                        for celda in range(barco.len):
                            tablero[fila-celda, col] = barco
                            barco.coordenadas.append([fila-celda, col])
                        break
            elif orientacion == 'E':

                if col + (barco.len -1) > tablero-1:
                    continue
                else:
                    for cell in range(barco.len):
                        if tablero[fila, col+cell] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(barco.len):
                            tablero[fila, col+cell] = barco
                            barco.coordinadas.append([fila, col+celda])
                        break
            if orientacion == 'S':
                if fila + (barco.len -1) > tablero-1:
                    continue
                else:
                    for celda in range(barco.len):
                        if tablero[fila+celda, col] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(barco.len):
                            tablero[fila+cell, col] = barco
                            barco.coordenadas.append([fila+celda, col])
                        break
            elif orientacion == 'O':
                if col - (barco.len -1) < 0:
                    continue
                else:
                    for celda in range(barco.len):
                        if tablero[fila, col-celda] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for cell in range(barco.len):
                            tablero[fila, col-cell] = barco
                            barcos.coordenadas.append([fila, col-celda])
                        break
