from nodoDato import Dato

class Lista:
    def __init__(self):
        self.inicio=None

    def add(self, dato, x, y):
        nuevo=Dato(dato,x,y)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            temp=self.inicio
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente=nuevo

    def length(self):
        contador=1
        temp=self.inicio
        while temp.siguiente is not None:
            contador += 1
            temp = temp.siguiente            
        return contador    

    def toString(self):
        temp=self.inicio
        while temp.siguiente is not None:
            print(temp.dato)
            temp = temp.siguiente  