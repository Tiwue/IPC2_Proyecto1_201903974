from listaDatos import Lista
from listaMatrices import ListaM
from graphviz import Digraph
from graphviz import Source

matrices=ListaM()
reducidas=ListaM()

def validarDimensiones(root):
    
    print("Validando dimensiones de las matrices...")
    for element in root:
        n = element.attrib['n']
        m = element.attrib['m']
        
        for subelement in element:
            if int(subelement.attrib['x']) > int(n):
                print("Error la cantidad de filas es mayor a las dimensiones definidas en: " + element.attrib['nombre'])
                return False
            elif int(subelement.attrib['y']) > int(m):
                print("Error la cantidad de columnas es mayor a las dimensiones definidas en: " + element.attrib['nombre'])
                return False
            else:
                continue
          
    return True  



def crearLista(root):
    print("Iniciando carga de datos en memoria")
    
    for element in root:
        datos=Lista()
        for subelement in element:
            dato=subelement.text
            x=subelement.attrib['x']
            y=subelement.attrib['y']
            identidad=0
            if int(dato) != 0:
                identidad=1
            datos.add(int(dato),int(x),int(y),identidad)
        nombre=element.attrib['nombre']
        n=element.attrib['n']
        m=element.attrib['m']
        matrices.add(nombre,n,m,datos,None)

    global reducidas
    reducidas=matrices.reducir()
   
    print("Datos Cargados en memoria....")        
    

def generarXML():
    reducidas.generarXML()
    
def generarGraficas():
    global reducidas
    print("\nIngrese el numero de la matriz que desea graficas:\n")
    reducidas.getName()
    numero=input()
    matriz=reducidas.getMatriz(numero)
    inicio = "digraph G { n[label=\"n="+str(matriz.n)+"\"]m[label=\"m="+str(matriz.m)+"\"]titulo [shape=diamond, label=\"matrices\"];matrix [label=<<table color='orange' cellspacing='0'>"
    tabla=matriz.generarTabla()
    fin="</table>>, shape=none]matriz[label=\""+matriz.nombre+"\"]titulo -> matriz;matriz -> n;matriz -> m;matriz -> matrix}"
    temp=inicio+tabla+fin
    s = Source(temp, filename="test", format="png")
    s.view()

def procesar(root):
    valida = validarDimensiones(root)
    if valida == True:
        print("Dimensiones correctas...")  
        crearLista(root)
        
    else:
        print("Intente cargar un nuevo archivo")    