import numpy as np
import random

import variables as vs

class Tablero :

    def __init__(self,identificacion):
        self.id=identificacion
        self.vidas=0
        self.dimension=10
        self.tablero=np.full((self.dimension, self.dimension), vs.agua)
        self.tablero_disparos=np.full((self.dimension, self.dimension), vs.agua)
        self.paco=Pintor() # Paco nos ayuda a ver el mundo mas bonito :)
    
    def mostrar_tablero(self):
        self.paco.pintar_tablero(self.tablero)

    def mostrar_tablero_disparos(self):
        self.paco.pintar_tablero(self.tablero_disparos)

    def añadir_barco(self,posiciones):
        for posicion in posiciones:
            self.tablero[posicion]= vs.barco
        self.vidas+=len(posiciones)

    def añadir_tocado(self,posicion):
            self.tablero_disparos[posicion]= vs.tocado

    def añadir_fallido(self,posicion):
            self.tablero_disparos[posicion]= vs.fallido  

    def posible_disparo(self,posicion):
        i=posicion[0]
        j=posicion[1]
        if i>=0 and i<self.dimension and j>=0 and j<self.dimension:
            return (self.tablero_disparos[posicion]!=vs.tocado or self.tablero_disparos[posicion]!=vs.fallido)
        else:
            print("Disparo erroneo")
            return False
    
    def disparo(self,posicion):
        if self.tablero[posicion]==vs.barco:
            self.tablero[posicion]=vs.tocado
            self.vidas-=1
            return True
        else:
            self.tablero[posicion]=vs.fallido
            return False
            
    def vivo(self):
        return (not self.vidas==0)   

class Pintor:

    def pintar_tablero(self, tablero):
        i = 0
        for fila in tablero:
            linea = ""
            for celda in fila:
                linea += celda + " "
            print(linea + str(i))
            i += 1
        lineax = ""
        for i in range(10):
            lineax += str(i) + " "
        print(lineax + "+")