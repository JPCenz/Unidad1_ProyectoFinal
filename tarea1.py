import os, pandas as pd

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero') 
    return num
def menu_principal():
    opcion = 0
    while opcion != range (1,11):
        print('================= TAREA 1 ===================')
        print('=============================================')
        print("1.  Leer archivos de disco duro")
        print("2.  Listar libros")
        print("3.  Agregar ibro")
        print("4.  Eliminar libro")
        print("5.  Buscar libro por ISBN") 
        print("6.  Ordenar libro por Titulo")  
        print("7.  Buscar libro por autor,editorial o genero")
        print("8.  Buscar libro por numero de autores")
        print("9.  Editar o actualizar datos de un libro")
        print("10. Guardar libros en archivo de disco duro")
        print("11. Salir del programa")
        print('=============================================')
        print ("Elige una opcion :")
        opcion = pedirNumeroEntero()
        return opcion
def main():
    while True:
        opcion = menu_principal()
        if opcion == 1:
            os.system('cls')
            print ("Opcion 1")   
            os.system('pause')
        elif opcion == 2:
            os.system('cls')
            print ("Opcion 2")
            os.system('pause')
        elif opcion == 3:
            os.system('cls')
            print("Opcion 3")
            os.system('pause')
        elif opcion == 4:
            os.system('cls')
            print("Opcion 4")
            os.system('pause')
        elif opcion == 5:
            os.system('cls')
            print("Opcion 5")
            os.system('pause')
        elif opcion == 6:
            os.system('cls')
            print("Opcion 6")
            os.system('pause')
        elif opcion == 7:
            os.system('cls')
            print("Opcion 7")
            os.system('pause')
        elif opcion == 8:
            os.system('cls')
            print("Opcion 8")
            os.system('pause')
        elif opcion == 9:
            os.system('cls')
            print("Opcion 9")
            os.system('pause')
        elif opcion == 10:
            os.system('cls')
            print("Opcion 10")
            os.system('pause') 
        elif opcion == 11:
            print("SALIR")
            break       
        else:
            os.system('cls')
            print("Ingresa un nuevo numero :")
    
if __name__ == '__main__':
    main()