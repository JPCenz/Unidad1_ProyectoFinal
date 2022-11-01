import os, pandas as pd
from numpy import append


class Libro:
    __id :str
    __titulo : str
    __genero = str
    __isbn : str
    __editorial : str
    __autor : list

    def __init__(self,id,titulo,genero,isbn,editorial) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def titulo(self, genero: str):
        self.__genero = genero

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn
    
    @property
    def editorial(self):
        return self.__editorial
    @editorial.setter
    def editorial(self, editorial: str):
        self.__editorial = editorial

    @property
    def autor(self):
        return self.__autor  
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    def __del__(self):
        pass


for i in range(3):
    a = Libro("001","ABCtitulo","comedia","00123","santillana")
    listalibros =[]
listalibros.append(a)




def ord_por_titulo(list_libros : list):
    list_ordenada = []
    for i in list_libros:
        list_ordenada.append(i)
    
    return list_ordenada
listafinal = ord_por_titulo(listalibros)

for i in listafinal:
    print(i)
































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