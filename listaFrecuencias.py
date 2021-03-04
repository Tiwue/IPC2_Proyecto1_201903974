from nodoFrecuencias import Frecuencia

class listaFrecuencias:
    def __init__(self):
        self.inicio=None

    def add(self, frec, grupo):
        nuevo=Frecuencia(frec,grupo)
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
            print(temp.frecuencia)
            temp = temp.siguiente  
        
    def getFrecuencia(self,grupo):
        temp=self.inicio
        while temp is not None:
            if int(temp.grupo) == grupo:
                return temp.frecuencia
            temp=temp.siguiente     
        return None

