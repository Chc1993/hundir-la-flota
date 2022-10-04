#importar librerias que se van a utilizar en el proceso

import numpy as np
import random

#Variables constantes del juego que serán utilizadas para el diseño de programación del juego
agua = "~"
barco = 'O'
barco_tocado = "@"
disparo_fallido = 'X'
medida_tablero= 10

#Diccionario para crear los barcos diferenciado por número de barcos y su tamaño
barcos = {"Barco de 1 eslora": (4, 1), "Barco de 2 esloras" : (3, 2),
"Barco de 3 esloras": (2, 3), "Barco de 4 esloras" : (1, 4)}

#definición d las clases
class Jugador:
    '''
    Definición de una clase jugador que diferenciará que tipo de jugador es:
     un humano o una máquina y que será fundamental para posteriormente seguir un 
     orden de turnos
    '''
    def __init__(self, tipo):
        self.tipo = tipo

class Tablero:
    '''
    Definición de una clase con dos atributos:
    - Uno son las medidas del trablero
    - El segundo es la creación del propio tablero relleno con la variable agua
    '''
    def __init__(self, medida = medida_tablero):
        self.medida = (medida_tablero, medida_tablero)
        
    def crear_tablero():
        return np.full((medida_tablero, medida_tablero), agua)
    
class Barco:
    '''
    Definición de una clase barco que estará definida por el nombre, tipo de barco y las coordenadas donde estará situado
    '''
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.len = barcos[tipo][1]
        self.coordenadas = []
        

def disparo(jugador: Jugador, tablero: Tablero): #función para declarar un disparo
    if jugador.tipo == "Humano":
        while 1:#Bucle para cerciorarse de que las coords están dentro del tablero
            while 1:#Bucle para cerciorarse de que las coordenadas escritas tienen sentido dentro de la lógica del juego
                try:
                    fila, col = [int(coord) for coord in input("Por favor, escribe unas coordenadas (separadas por un espacio) para poder disparar").split()]
                    break #salida del segundo while
                except ValueError:
                    print("Las coordenadas introducidas no son válidas")
            if (fila < 0 or fila > 9) or (col < 0 or col > 9):
                print("Las coordenadas introducidas están fuera del tablero")
            else:
                break #salida del primer while
    else: #disparo aleatorio de la máquina
        fila = random.randint(0,medida_tablero-1)
        col = random.randint(0,medida_tablero-1)
    
    if tablero[fila, col] == barco:
        print("BARCO TOCADO")
        tablero[fila, col] = barco_tocado #Barco tocado será representado con @ en dicha fila y columna
        if barco not in barco:#Si no hay más barcos sobre el tablero que declare el final del juego y el ganador
            fin_juego()
        #Si no, y hay barcos todavía, sigue la partida
        disparo(jugador, tablero)
    elif tablero[fila, col] == agua: #Disparo fallido
        print("AGUA")
        tablero[fila, col] = disparo_fallido
    elif tablero[fila, col] == barco_tocado or tablero[fila, col] == disparo_fallido:
        print("Ya has disparado en estas coordenadas!")
        disparo(jugador, tablero)
        
def menu(): #función que declara un menú para que el jugador humano decida qué hacer durante su turno
    print('''Opciones de juego:
          1. disparar
          2. Mirar tu tablero
          3. Mirar tablero rival
          4. salir''')

def fin_juego(tablero1: Tablero, tablero2: Tablero):#función para declarar cuándo el juego ha terminado(es decir, si hay barcos en el tablero del jugador humano, significa que ha ganado la partida, si no es que ha ganado la máquina)
    if barco in tablero1:
        print("Enhorabuena! Has ganado")
        exit() 
    else:
        print("Lo siento. Has perdido")
        exit() 

def crear_flota(tablero: Tablero):
    flota = []
    for i in barcos.keys():
        for num in range(barcos[i][0]): 
            barco_nuevo = Barco(i + str(num), i)
            situar_barco(barco_nuevo, tablero)
            flota.append(barco_nuevo)
    return flota

def situar_barco(bote: Barco, tablero: Tablero):
    situado = False
    orientaciones = ['N', 'E', 'S', 'O']
    
    while not situado:
        fila = random.randint(0,medida_tablero-1)
        col = random.randint(0,medida_tablero-1)
        orientacion = random.choice(orientaciones)

        if tablero[fila, col] == agua:
            if orientacion == 'N':
                if fila - (bote.len -1) < 0:
                    #Si fila - (barco.len -1) es menor que 0 significa que el barco  está en el lado norte del tablero
                    continue
                else: #comporbar si el barco puede situarse
                    for celda in range(bote.len):
                        if tablero[fila-celda, col] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break #Si puede situarse, el barco se coloca y salir del bucle
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila-celda, col] = barco
                            bote.coordenadas.append([fila-celda, col]) 
                        break
                    
            elif orientacion == 'E':
                
                if col + (bote.len -1) > medida_tablero-1:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila, col+celda] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila, col+celda] = barco
                            bote.coordenadas.append([fila, col+celda]) 
                        break
                    
            if orientacion == 'S':
                
                if fila + (bote.len -1) > medida_tablero-1:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila+celda, col] == agua:
                            placed = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila+celda, col] = barco
                            bote.coordenadas.append([fila+celda, col]) 
                        break

            elif orientacion == 'W':
                
                if col - (bote.len -1) < 0:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila, col-celda] == agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila, col-celda] = barco
                            bote.coordenadas.append([fila, col-celda]) 
                        break
                    
#crear jugadores
if __name__ == '__main__': 
    jugador1 = Jugador("Humano")
    jugador2 = Jugador("Máquina")
#crear tableros
    tablero = Tablero 
    mi_tablero = tablero.crear_tablero()
    tablero_rival = tablero.crear_tablero()
#crear flotas
    mis_barcos = crear_flota(mi_tablero)
    barcos_rival = crear_flota(tablero_rival)


