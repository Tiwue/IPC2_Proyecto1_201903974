from listaDatos import Lista

class ListaMatrices:

    def __init__(self,nombre,n,m,datos,frecuencias):
        self.nombre=nombre
        self.n=n
        self.m=m
        self.datos=datos
        self.siguiente=None
        self.frecuencias=frecuencias
      