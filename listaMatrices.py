from nodoListaMatrices import ListaMatrices
from listaDatos import Lista
from listaFrecuencias import listaFrecuencias
from procesamiento import reducidas

class ListaM:
    def __init__(self):
        self.inicio=None

    def add(self, nombre, n, m,lista):
        nuevo=ListaMatrices(nombre,n,m,lista,None)
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

    def imprimir(self):
        temp=self.inicio
        while temp is not None:
            temp.datos.toString()
            temp = temp.siguiente  

            
    def reducir(self):
        temp=self.inicio
        
        while temp is not None:
            i=1
            datosredus=Lista()
            while temp.n >= i:
                frecs=1
                k=i+1
                while temp.n >k:
                    j=1
                    coincidencias=0
                    while j<=temp.m:
                        
                        arriba=temp.datos.getIdentidad(i,j)
                        abajo=temp.datos.getIdentidad(k,j)
                        if arriba !=None and abajo !=None:
                            if arriba == abajo:
                                coincidencias += 1
                        j += 1  

                    if coincidencias== temp.m:
                        h=1           
                                       
                        while h<=temp.m:
                            arriba=temp.datos.getDato(i,h)
                            abajo=temp.datos.getDato(k,h)
                            nuevoDato=arriba+abajo
                            datosredus.add(nuevoDato,i,h,temp.datos.getIdentidad(i,h))##corregir coordenadas
                            temp.datos.eliminar(k,h)
                            
                            h += 1  
                        frecs +=1
                    k += 1
                i +=1
            temp = temp.siguiente        