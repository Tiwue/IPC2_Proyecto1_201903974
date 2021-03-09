from nodoListaMatrices import ListaMatrices
from listaDatos import Lista
from listaFrecuencias import listaFrecuencias
import xml.etree.ElementTree as ET


class ListaM:
    def __init__(self):
        self.inicio=None

    def add(self, nombre, n, m,lista,frecuencias):
        nuevo=ListaMatrices(nombre,n,m,lista,frecuencias)
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
                
                h=1
                if temp.datos.getDato(i,1) != None:
                    frecuencias.add(frecs,index+1)
                    index += 1   
                while h<=int(temp.m):
                    if temp.datos.getDato(i,h) != None:
                        dato=temp.datos.getDato(i,h)
                        identidad=temp.datos.getIdentidad(i,h)
                        datosredus.add(dato,index,h,identidad)
                    h+=1
                i +=1
            reducidas.add("Matriz",index,temp.m,datosredus,frecuencias)
            temp = temp.siguiente        
        return reducidas    


    def isEmpty(self):
        temp=self.inicio
        if temp == None:
            return True
        return False

    def vaciar(self):
        if self.inicio is not None:
            self.inicio.siguiente = None
            self.inicio =None    
            
    def generarXML(self):
        
        temp=self.inicio
        root = ET.Element('matrices')
        while temp is not None:
            print("Generando arbol de elementos...")
            matriz = ET.SubElement(root,'matriz')
            matriz.set('nombre',temp.nombre)
            matriz.set('n',str(temp.n))
            matriz.set('m',str(temp.m))
            matriz.set('g',str(temp.n))
            temp.datos.XML(matriz)
            temp.frecuencias.XML(matriz)
            temp=temp.siguiente
        print("Datos obtenidos con exito...")
        misdatos=ET.tostring(root)
        print("transformando datos a cadena...")
        myfile=open("matrizReducida.xml", "wb")
        print("Creando archivo...")
        myfile.write(misdatos)
        print("Datos escritos con exito...")
        myfile.close()

    def getName(self):
        temp=self.inicio
        num=1
        while temp is not None:
            print(str(num)+"." + temp.nombre)
            num+=1
            temp = temp.siguiente           

    def getMatriz(self,numero):
        temp=self.inicio
        num=1
        while temp is not None:
            if int(numero)==num:
                return temp
            num +=1
            temp=temp.siguiente        

    