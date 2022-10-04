import numpy as np

#Arranque del juego
while (barco in mi_tablero and barco in tablero_rival):
        #Turno jugador humano
        while 1:
            menu()
            while 1:
                try:
                    opcion = int(input("Elige una opción "))
                    break
                except ValueError:
                    print("Esa opción no es valida")
                    pass
            if opcion == 1:
                disparo(jugador1 ,tablero_rival)
                break
            elif opcion == 2:
                print(mi_tablero) #Ver tablero propio
                continue
            elif opcion == 3:
                print(tablero_rival) #Ver el tablero rival
                continue
            elif opcion == 4:
                exit()
            else:
                print("Esa opción no existe. Prueba de nuevo")
                continue
        
        #Turno contrincante
        print('Turno del contrincante')
        disparo(jugador2, mi_tablero)
        
    #Fin del juego
fin_juego(mi_tablero, tablero_rival)