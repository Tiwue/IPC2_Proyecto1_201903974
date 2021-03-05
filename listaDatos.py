from nodoDato import Dato

class Lista:
    def __init__(self):
        self.inicio=None

    def add(self, dato, x, y,identidad):
        nuevo=Dato(dato,x,y,identidad)
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
        
        while temp is not None:
            print(temp.dato)
            temp = temp.siguiente  
        
    def getDato(self,x,y):
        temp=self.inicio
        while temp is not None:
            if int(temp.x) == x and int(temp.y)==y:
                return temp.dato
            temp=temp.siguiente     
        return None

    def getIdentidad(self,x,y):
        temp=self.inicio
        while temp is not None:
            if int(temp.x)==x and int(temp.y)==y:
                return temp.identidad
            temp=temp.siguiente
        return None

    def eliminar(self, x,y):
        temp = self.inicio
        prev = None
        encontrado= False
        while not encontrado:
           if int(temp.x) == x and int(temp.y)==y:
               encontrado=True
           else:
               prev = temp
               temp = temp.siguiente
        if prev == None:
            self.inicio=temp.siguiente
        else:
            prev.siguiente=temp.siguiente               

    def setDato(self,x,y,dato):
        temp=self.inicio
        while temp is not None:
            if int(temp.x) == x and int(temp.y)==y:
                temp.dato = dato
            temp=temp.siguiente 
      