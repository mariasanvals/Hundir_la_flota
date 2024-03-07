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
    
    def mostrar_tablero(self):
        print(self.tablero)

    def mostrar_tablero_disparos(self):
        coordenada_x = np.array([[0,1,2,3,4,5,6,7,8,9]])
        coordenada_y = np.transpose([[0,1,2,3,4,5,6,7,8,9,"-"]])
        tab_1 = np.vstack((self.tablero_disparos,coordenada_x))
        tab_2 = np.column_stack((tab_1,coordenada_y))
        print(tab_2)

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
            self.tablero[posicion]==vs.tocado
            self.vidas-=1
            return True
        else:
            self.tablero[posicion]==vs.fallido
            return False
        
    def mostrar_disparo(self,posicion):
        if self.tablero[posicion]==vs.barco:
            self.tablero[posicion]=vs.tocado
        else:
            self.tablero[posicion]=vs.fallido
            
    def vivo(self):
        return (not self.vidas==0)   

