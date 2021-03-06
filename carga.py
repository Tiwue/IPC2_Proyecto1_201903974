import xml.etree.ElementTree as ET
from procesamiento import matrices
from procesamiento import reducidas
def cargar():
    print("Ingrese la ruta del archivo:")
    ruta=input()
    if matrices.isEmpty()==True:
        tree=ET.parse(ruta)
    else:
        matrices.vaciar()
        matrices.reducir()
        tree=ET.parse(ruta)
    return tree