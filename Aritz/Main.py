
import sys

from Funciones import *
from Clases import *
from Variables import *
 

def main():
    print("¡Bienvenido a Hundir la Flota! Dispondrás de un tablero con: \
    \n 4 barcos de 1 posición de eslora \
    \n 3 barcos de 2 posiciones de eslora \
    \n 2 barcos de 3 posiciones de eslora \
    \n 1 barco de 4 posiciones de eslora. \
    \n\n Los barcos se posicionarán aleatoriamente en el tablero, al igual que los de la maquina.")
    tablero_jug=Tablero()
    print("Así queda tu tablero de barcos:\n",tablero_jug.mostrar_tablero())
    tablero_maquina=Tablero()
    print("\nEste es el tablero de tu contrincante:\n",tablero_maquina.mostrar_tablero())
    print("\nEl juego es sencillo. Tendrás que ir introduciendo coordenadas por pantalla, " +
    "hasta que hundas todos los barcos del rival.\n\nLas coordenadas se introducen separandolas" +
    " por puntos. Por ejemplo, si queremos la disparar a la primera fila, columna 8, introduciríamos" +
    " por pantalla '1,8'.\n\n¿Listo? A jugar!")
    
    print("Ahora, colocarás los 4 barcos de 1 posición de eslora:")
    for i in range(4):
        crear_barco(tablero_jug,1)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás los 3 barcos de 2 posiciones de eslora:")
    for i in range(3):
        crear_barco(tablero_jug,2)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás los 2 barcos de 3 posiciones de eslora:")
    for i in range(2):
        crear_barco(tablero_jug,3)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás el barco de 4 posiciones de eslora:")
    for i in range(1):
        crear_barco(tablero_jug,4)
        print("Tu tablero va a ser: ",tablero_jug.mostrar_tablero)
        tablero.mostrar_tablero()
    print("Es turno de que la máquina coloque sus barcos")
    for i in range(4):
        crear_barco(tablero_maquina,1,aleatorio=True)
    for i in range(3):
        crear_barco(tablero_maquina,2,aleatorio=True)
    for i in range(2):
        crear_barco(tablero_maquina,3,aleatorio=True)
    for i in range(1):
        crear_barco(tablero_maquina,4,aleatorio=True)
    print("\n\n Listo")
    turno="jugador"
    while turno!="Fin":
        if turno=="jugador":
            print("Es tu turno, es hora de disparar.")
            tablero_a_disparar=tablero_maquina
        else:
            print("Es turno de que dispare la máquina")
            tablero_a_disparar=tablero_jug
        turno=disparo(tablero_a_disparar,turno)


    

main()