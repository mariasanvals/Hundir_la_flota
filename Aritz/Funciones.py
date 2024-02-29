import numpy as np
import random

from Variables import *

def disparo(tablero,jugador):
    valido=False
    while not valido:
        if jugador=="Maquina":
            posicion=(random.randint(0, tab.dimension-1),random.randint(0, tab.dimension-1))
        else:
            posicion=tuple(int(x) for x in input("Introduce las coordenadas donde quieres disparar separadas por una coma").split(","))
        valido=posible_disparo(tablero,posicion)
    dado=tablero.disparo(posicion)
    print("Disparando...")
    if dado:
        turno=jugador
        if jugador=="Maquina":
            print("\nNOS HA IMPACTADO DE LLENO!!! Le vuelve a tocar a la maquina")
        else:
            print("\n¡BOOM! TOCADO! Has impactado en un barco de la máquina.\n\n¡Te sigue tocando!")
    else:
        if jugador=="Maquina":
            turno="Maquina"
            print("\n¡Ha fallado! Nos vuelve a tocar")
        else:
            turno="player"
            print("\n¡AGUA! Has fallado. Le toca a la maquina")
    if tablero.vidas():
        return turno
    else:
        if jugador=="Maquina":
            print("\n¡LOSER! Has palmado. Tienes que practicar un poco más")
        else:
            print("\n¡GANASTE! Enhorabuena, eres un auténtico grumete!")
        return "Fin"
    



def posicion_correcta(tablero,posicion,orientacion,n):
        correcta=True
        i=posicion[0]
        j=posicion[1]
        if i<0 or i>tablero.dimension-1 or j<0 or j>tablero.dimension-1:
            print("La posición indicada está fuera del tablero")
            correcta=False
        else:
            if orientacion=="N" and j-n+1<0:
                print("El barco se sale del tablero")
                correcta=False
            elif orientacion=="S" and j+n-1>tablero.dimension:
                print("El barco se sale del tablero")
                correcta=False
            elif orientacion=="E" and i+n-1>tablero.dimension:
                print("El barco se sale del tablero")
                correcta=False
            elif orientacion=="O" and i-n+1<0:
                print("El barco se sale del tablero")
                correcta=False
        return correcta
    
def posicion_correcta_notexto(tablero,posicion,orientacion,n):
        correcta=True
        i=posicion[0]
        j=posicion[1]
        if i<0 or i>tablero.dimension-1 or j<0 or j>tablero.dimension-1:
            correcta=False
        else:
            if orientacion=="N" and j-n+1<0:
                correcta=False
            elif orientacion=="S" and j+n-1>tablero.dimension:
                correcta=False
            elif orientacion=="E" and i+n-1>tablero.dimension:
                correcta=False
            elif orientacion=="O" and i-n+1<0:
                correcta=False
        return correcta

def crear_barco(tablero,n,aleatorio=False):
        valido=False
        while not valido:
            if aleatorio==True:
                orientacion=random.choice(ORIENTACIONES)
                posicion=(random.randint(0, tab.dimension-1),random.randint(0, tab.dimension-1))
                while not posicion_correcta_notexto(tablero,posicion,orientacion,n):
                    posicion=(random.randint(0, tablero.dimension-1),random.randint(0, tablero.dimension-1))
                posiciones=[(random.randint(0, tablero.dimension-1),random.randint(0, tablero.dimension-1))]
                    
            else:
                posicion=tuple(int(x) for x in input("Introduce las coordenadas del barco separadas por una coma").split(","))
                if n==1:
                    orientacion="N"
                else:
                    orientacion=input("Introduce la orientación del barco ('N','S','E','O')").upper()
                while not posicion_correcta(tablero,posicion,orientacion,n) or orientacion not in ORIENTACIONES:
                    posicion=tuple(int(x) for x in input("Introduce las coordenadas del barco separadas por una coma").split(","))  
                    if n==1:
                        rientacion="N"
                    else:
                        orientacion=input("Introduce la orientación del barco ('N','S','E','O')").upper()
                posiciones=[posicion]
            for i in range(n-1):
                if orientacion=="N":
                    nueva_posi=(posiciones[-1][0]-1,posiciones[-1][1])
                    posiciones.append(nueva_posi)
                elif  orientacion=="S":
                    nueva_posi=(posiciones[-1][0]+1,posiciones[-1][1])
                    posiciones.append(nueva_posi)
                elif orientacion=="E":
                    nueva_posi=(posiciones[-1][0],posiciones[-1][1]+1)
                    posiciones.append(nueva_posi)
                else:
                    nueva_posi=(posiciones[-1][0],posiciones[-1][1]-1)
                    posiciones.append(nueva_posi)
            c=0
            for posicion in posiciones:
                if  posicion_correcta_notexto(tablero,posicion,orientacion,n) and tablero.tablero[posicion]!="O":
                    c+=1
            if c==n:
                valido=True
        
        tablero.añadir_barco(posiciones)
        
        
