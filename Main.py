#C:\Users\steve\Desktop\prueba.xml
from pip._vendor.distlib.compat import raw_input
from carga import cargar
from procesamiento import procesar

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
        print("Procesanding Archivo:")
        if root is not None:
            procesar(root)
        else:
            print("Debe cargar un archivo primero")    
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="3":
        print("Escribir archivo del estudiante")
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="4":
        print("Datos Mios :D")
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="5":
        print("Generar Gráfica")
        raw_input("\nPresiona la tecla Enter para continuar")
    elif lectura=="6":
        print("Off :C")
        on=False
    else:
        print("Error: Debe Ingresar una opcion valida")                

   