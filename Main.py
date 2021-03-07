#C:\Users\steve\Desktop\prueba.xml
from pip._vendor.distlib.compat import raw_input
from carga import cargar
from procesamiento import procesar
from procesamiento import generarXML
from procesamiento import generarGraficas
on=True
root=None
tree=None
while(on==True):
    print("\nMenu Principal: \n1.Cargar archivo\n2.Procesar archivo\n3.Escibir archivo salida\n4.Mostrar datos del Estudiante\n5.Generar gráfica\n6.Salida")
    lectura=input("Eliga una Opción:\n")
    if lectura=="1":
        print("Cargar Archivo:")
        try:
            tree = cargar()
            root= tree.getroot()
            print("Archivo subido correctamente")
                        
            raw_input("\nPresiona la tecla Enter para continuar")
        except:
            print("No fue posible leer el archivo Seleccionado...")
            raw_input("\nPresiona la tecla Enter para continuar")    
        
    elif lectura=="2":
        print("Procesando Archivo:")
        if root is not None:
            procesar(root)
        else:
            print("Debe cargar un archivo primero")    
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="3":
        generarXML()
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="4":
        print("Steven Josue González Monroy\n201903974\nIntroduccion a la Programacion y Computacion 2 Seccion D\nIngenieria en Ciencias y Sistemas")

        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="5":
        generarGraficas()
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="6":
        print("Off :C")
        on=False
    else:
        print("Error: Debe Ingresar una opcion valida")                

   