# VARIABLES 

import numpy as np

tablero = np.full((10,10))

barcos = {
    "barcos_1_eslora": 4,
    "barcos_2_Eslora": 3,
    "barcos_3_eslora": 2,
    "barcos_4_eslora": 1
}
"""
4 barcos de 1 posición de eslora
3 barcos de 2 posiciones de eslora
2 barcos de 3 posiciones de eslora
1 barco de 4 posiciones de eslora
"""





# CLASES

#from variables import *

class Tablero:

    def __init__(self,id_jugador, dimensiones_tablero,barcos, tablero_barcos, tablero_disparos):

        self.id_jugador = id_jugador
        self.dimensiones_tablero = tablero
        self.barcos = barcos
        self.tablero_barcos = np.zeros(self.dimensiones_tablero, dtype=int)
        self.tablero_disparos = np.zeros(self.dimensiones_tablero, dtype=int)

    def posicion_barco_aleatorio(tablero, longitud):
            #Iniciamos un bucle while que se ejecutará indefinidamente hasta que se cumpla cierta condición. 
            #En este caso, el bucle seguirá ejecutándose hasta que se logre posicionar el barco correctamente 
            #en el tablero.
        while True:
            fila = random.randint(0, self.dimensiones_tablero[0] - 1)   #posición fila aleatoria
            columna = random.randint(0,  self.dimensiones_tablero[1] - 1)   #posición columna aleatoria
            orientacion = random.choice(["N", "S", "E", "O"])   #te da aleatoriamente una orientación

            posiciones = []

            for i in range(longitud):
                if orientacion == "N" and fila - i >= 0:
                    posiciones.append((fila - i, columna))
                elif orientacion == "S" and fila + i < self.dimensiones_tablero[0]:
                    posiciones.append((fila + i, columna))
                elif orientacion == "E" and columna + i < self.dimensiones_tablero[1]:
                    posiciones.append((fila, columna + i))
                elif orientacion == "O" and columna - i >= 0:
                    posiciones.append((fila, columna - i))
                else:
                    break
            print(f"Tentativa: {fila}, {columna}, {orientacion}, {posiciones}")
    ### Verificamos si la longitud de las posiciones es igual a la longitud esperada del barco y si todas
            # las posiciones en el tablero están vacías (es decir, " "). Si ambas condiciones son verdaderas, 
            #significa que podemos colocar el barco en estas posiciones.
            if len(posiciones) == longitud and all(tablero[pos] == " " for pos in posiciones):
                for pos in posiciones:
                    tablero[pos] = "O"
                break

     # Coloca el barco en el tablero
            for i, j in posiciones:
                self.tablero_barcos[i, j] = 1           

    def disparar_coordenada(self, x, y):
            # Verifica si hay un barco en las coordenadas dadas
            if self.tablero_barcos[x, y] == 1:
                print("¡Impacto!")
                self.tablero_barcos[x, y] = 2  # Marca el impacto en el tablero de barcos
                self.tablero_disparos[x, y] = 1  # Marca el impacto en el tablero de disparos
            else:
                print("Agua...")
                self.tablero_disparos[x, y] = 2  # Marca el agua en el tablero de disparos






# FUNCIONES

#from variables import *
#from clases import *
        
import random 

def construir_tablero(dimension):
    return np.full((10,10),"")

def colocar_barcos(tablero, coordenadas):
    for coord in coordenadas:
        fila,columna = coord
        tablero[fila,columna] = "O"

barco_1 = [(0,1), (1,1)] 
barco_2 = [(1,3), (1,4), (1,5), (1,6)]

colocar_barcos(tablero,barco_1)
colocar_barcos(tablero,barco_2)

print(tablero)











# Recibe un disparo en uno de los barcos, sustituyendo la O por una X
def disparo(tablero, coordenadas):
        fila, columna = coordenadas
        if tablero[fila, columna] == "O":
            print("Has dado en un barco!!!!")
            tablero[fila, columna] = "X"

# Recibe un disparo en agua, sustituyendo uno de los espacios por un guión: -
        elif tablero[fila,columna] == "":
            print("Has disparado al agua :(")
            tablero[fila, columna] = "-"


disparo_1 = (1,1)
disparo_2 = (5,4)
disparo_3 = (1,0)

disparo(tablero, disparo_1)
disparo(tablero, disparo_2)
disparo(tablero, disparo_3)




