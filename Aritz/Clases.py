import numpy as np
import random

from Variables import *

class Tablero :

    def __init__(self,identificacion):
        self.id=identificacion
        self.vidas=0
        self.dimension=10
        self.tablero=np.full((self.dimension, self.dimension), " ")
        self.tablero_disparos=np.full((self.dimension, self.dimension), " ")
    
    def mostrar_tablero(self):
        print(self.tablero)

    def añadir_barco(self,posiciones):
        for posicion in posiciones:
            self.tablero[posicion]=BARCO
        self.vidas+=len(posiciones)

    def posible_disparo(self,posicion):
        i=posicion[0]
        j=posicion[1]
        if i>=0 and i<self.dimension and j>=0 and j<self.dimension:
            return (self.tablero_disparos[posicion]!="X" or self.tablero_disparos[posicion]!="-")
        else:
            return False
    
    def disparo(self,posicion):
        if self.tablero[posicion]==BARCO:
            self.tablero[posicion]==TOCADO
            self.vidas-=1
            return True
        else:
            self.tablero[posicion]==TIRO_AGUA
            return False
        
    def vivo(self):
        return (not self.vidas==0)
    
    

