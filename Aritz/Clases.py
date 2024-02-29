import numpy as np
import random

from Variables import *

class Tablero :

    def __init__(self) :
        self.vidas=0
        self.dimension=10
        self.tablero=np.full((self.dimension, self.dimension), " ")
    
    def mostrar_tablero(self):
        print(self.tablero)

    def añadir_barco(self,posiciones):
        for posicion in posiciones:
            self.tablero[posicion]=BARCO
        self.vidas+=len(posiciones)

    def posible_disparo(self,posicion):
        i=posicion[0]
        j=posicion[1]
        if i>0 and i<self.dimension-1 and j>0 and j<self.dimension-1:
            return (self.tablero[posicion]!="X")
        else:
            return False
    
    def disparo(self,posicion):
        if self.tablero[posicion]==BARCO:
            self.tablero[posicion]==TOCADO
            self.vidas-=1
            return True
        else:
            return False
        
    def vivo(self):
        return (not vidas==0)
    
    

