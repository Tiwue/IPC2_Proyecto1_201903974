from listaDatos import Lista
from listaMatrices import ListaM

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
        matrices.add(nombre,n,m,datos)

    reducidas=matrices.reducir()
    reducidas.imprimir()
    print("Datos Cargados en memoria....")        
    



def procesar(root):
    valida = validarDimensiones(root)
    if valida == True:
        print("Dimensiones correctas...")  
        crearLista(root)
        
    else:
        print("Intente cargar un nuevo archivo")    