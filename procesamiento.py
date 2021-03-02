from listaDatos import Lista



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
    datos=Lista()
   
    for element in root:
        for subelement in element:
            dato=subelement.text
            x=subelement.attrib['x']
            y=subelement.attrib['y']
            datos.add(dato,x,y)
    datos.toString()


def procesar(root):
    valida = validarDimensiones(root)
    if valida == True:
        crearLista(root)
    else:
        print("Intente cargar un nuevo archivo")    