import xml.etree.ElementTree as ET

def cargar():
    print("Ingrese la ruta del archivo:")
    ruta=input()
    tree=ET.parse(ruta)
    return tree