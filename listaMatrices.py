from nodoListaMatrices import ListaMatrices
from listaDatos import Lista
from listaFrecuencias import listaFrecuencias


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
        reducidas=ListaM()
        while temp is not None:
            index=0
            i=1
            datosredus=Lista()
            frecuencias=listaFrecuencias()
            while int(temp.n) >= i:
                frecs=1
                k=i+1
                while int(temp.n) >=k:
                    j=1
                    coincidencias=0
                    while j<=int(temp.m):
                        
                        arriba=temp.datos.getIdentidad(i,j)
                        abajo=temp.datos.getIdentidad(k,j)
                        if arriba !=None and abajo !=None:
                            if arriba == abajo:
                                coincidencias += 1
                        j += 1  

                    if coincidencias== int(temp.m):
                        h=1           
                                
                        while h<=int(temp.m):
                            arriba=temp.datos.getDato(i,h)
                            abajo=temp.datos.getDato(k,h)
                            nuevoDato=arriba+abajo
                            temp.datos.setDato(i,h,nuevoDato)
                            temp.datos.eliminar(k,h)
                            
                            h += 1  
                        frecs +=1
                        
                    k += 1
                frecuencias.add(frecs,i)
                h=1
                if temp.datos.getDato(i,1) != None:
                    index += 1   
                while h<=int(temp.m):
                    if temp.datos.getDato(i,h) != None:
                        dato=temp.datos.getDato(i,h)
                        identidad=temp.datos.getIdentidad(i,h)
                        datosredus.add(dato,index,h,identidad)
                    h+=1
                i +=1
            reducidas.add("Ejemplo Salida",index,temp.m,datosredus)
            temp = temp.siguiente        
        return reducidas    