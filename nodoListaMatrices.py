from listaDatos import Lista

class ListaMatrices:

    def __init__(self,nombre,n,m,datos,frecuencias):
        self.nombre=nombre
        self.n=n
        self.m=m
        self.datos=datos
        self.siguiente=None
        self.frecuencias=frecuencias

    def generarTabla(self):
        x=1
     
        initFila="<tr>"
        initColumna="<td>"
        finFila="</tr>"
        finColumna="</td>"
        tabla=""
        while x <= int(self.n):
            tabla=tabla+initFila
            y=1
            while y<=int(self.m):
                date=self.datos.getDato(x,y)
                tabla=tabla+initColumna+str(date)+finColumna
                y+=1
            tabla=tabla+finFila
            x+=1    
        return tabla