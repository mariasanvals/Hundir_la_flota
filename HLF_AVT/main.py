
import sys

from funciones import *
from clases import *
from variables import *
 
import os
os.system('cls')

def main():
    print("¡Bienvenido a Hundir la Flota! Dispondrás de un tablero con: \
    \n 4 barcos de 1 posición de eslora \
    \n 3 barcos de 2 posiciones de eslora \
    \n 2 barcos de 3 posiciones de eslora \
    \n 1 barco de 4 posiciones de eslora.")
    tablero_jug=Tablero("Jugador")
    print("Este es tu tablero:\n")
    tablero_jug.mostrar_tablero()
    tablero_maquina=Tablero("Maquina")
    # print("\nEste es el tablero de tu contrincante:\n")
    # tablero_maquina.mostrar_tablero()
    print("Este es el tablero de tus disparos:\n")
    tablero_maquina.mostrar_tablero_disparos()
    print("\nEl juego es sencillo. Tendrás que ir introduciendo coordenadas por pantalla, " +
    "hasta que hundas todos los barcos del rival.\n\nLas coordenadas se introducen separandolas" +
    " por comas. Por ejemplo, si queremos disparar a la primera fila, columna 8, introduciríamos" +
    " por pantalla '1,8'.\n\n¿Listo? A jugar!")
    modo_aleatorio=input("¿Quieres colocar tus barcos de manera aleatoria?, Responde: 'Si' o 'No': ") == "Si"
    
    print("Ahora, colocarás los 4 barcos de 1 posición de eslora:")
    for i in range(4):
        crear_barco(tablero_jug,1,aleatorio=modo_aleatorio)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás los 3 barcos de 2 posiciones de eslora:")
    for i in range(3):
        crear_barco(tablero_jug,2,aleatorio=modo_aleatorio)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás los 2 barcos de 3 posiciones de eslora:")
    for i in range(2):
        crear_barco(tablero_jug,3,aleatorio=modo_aleatorio)
        tablero_jug.mostrar_tablero()
    print("Ahora, colocarás el barco de 4 posiciones de eslora:")
    for i in range(1):
        crear_barco(tablero_jug,4,aleatorio=modo_aleatorio)
        print("Tu tablero va a ser: ")
        tablero_jug.mostrar_tablero()
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
    turno="Jugador"
    while turno!="Fin":
        if turno=="Jugador":
            print("Es tu turno, es hora de disparar.")
            print("\n¿Dónde quieres disparar?:\n")
            tablero_maquina.mostrar_tablero_disparos()
            tablero_a_disparar=tablero_maquina
        else:
            print("Es turno de que dispare la máquina")
            print("Así está tu tablero de barcos:\n")
            tablero_jug.mostrar_tablero()
            tablero_a_disparar=tablero_jug
        turno=disparo(tablero_a_disparar)
  

main()