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
    print("\nIngrese el numero de la matriz que desea graficas:\n")
    reducidas.getName()
    numero=input()
    matriz=reducidas.getMatriz(numero)
    temp = """
    digraph G{
    Edge [dir=forward]
    node [shape=plaintext]

    0 [label="0 (None)"]
    0 -> 5 [label="root"]
    1 [label="1 (Hello)"]
    2 [label="2 (how)"]
    2 -> 1 [label="advmod"]
    3 [label="3 (are)"]
    4 [label="4 (you)"]
    5 [label="5 (doing)"]
    5 -> 3 [label="aux"]
    5 -> 2 [label="advmod"]
    5 -> 4 [label="nsubj"]
    }
    """
    s = Source(temp, filename="test", format="png")
    s.view()

def procesar(root):
    valida = validarDimensiones(root)
    if valida == True:
        print("Dimensiones correctas...")  
        crearLista(root)
        
    else:
        print("Intente cargar un nuevo archivo")    