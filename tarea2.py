import os

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
        print('================= TAREA 2 ===================')
        print('==============Menu principal=================')
        print('')
        print("1.  Listar pokemons por generación")
        print("2.  Listar pokemons por forma")
        print("3.  Listar pokemons por habilidad")
        print("4.  Listar pokemons por habitat")
        print("5.  Listar pokemons por tipo") 
        print("6.  SALIR")  
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
            print("SALIR")
            break       
        else:
            os.system('cls')
            print("Ingresa un nuevo numero :")
    
if __name__ == '__main__':
    main()