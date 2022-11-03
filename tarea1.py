import os,csv


class Libro:
    __id :str
    __titulo : str
    __genero : str
    __isbn : str
    __editorial : str
    __autor : list = []

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
    def genero(self, genero: str):
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
    def autor(self, autor :str):
        self.__autor=self.__autor.append(autor)
        autor = autor.strip()
        lista_temp =[]
        for a in autor.split(sep=","):
            lista_temp.append(a.strip())
        if len(lista_temp) >1:
            self.__autor = lista_temp
        else:
            self.__autor= [autor] 

    def __del__(self):
        pass











#lee un archivo csv y retorna una lista de objetos Libros
def abrir_archivo(file ="libros.csv" )-> list[Libro]:
    lista_libros=[]
    try:
        with open(file) as f:
            reader = csv.reader(f)
            line_count=0
            for row in reader:
                if line_count == 0:                   
                    line_count += 1
                else:
                    i = Libro(row[0],row[1],row[2],row[3],row[4])
                    autor = row[5]             
                    i.autor = autor
                    lista_libros.append(i)                   
                    line_count += 1
        return lista_libros
    except Exception as ex:
        print(ex)
        
#Recibe una lista de Libros y escribe los datos en un archivo .csv
def escribir_archivo(Libros: list[Libro],file='libros_guardados.csv')-> None :
    try:
        with open(file, 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Id","Titulo","Genero","ISBN","Editorial","Autor"])
            for l in Libros:
                autores = ','.join(l.autor)
                writer.writerow([l.id,l.titulo,l.genero,l.isbn,l.editorial,autores])
        print("Libros Guardados Exitosamente en el archivo libros_guardados.csv ")

    except Exception as ex:
        print(ex)
    
#Reciba una lista de objetos Libros imprime en pantalla sus atributpos
def listar_libros(list_libros : list[Libro] ) ->list[Libro]:
    print("==============================  Libros  ===============================================")
    print("Pos|     Titulo         |   Genero  |        ISBN    |   Editorial   |   Autor (es)")
    for i,libro in enumerate(list_libros,start=1):
        print(f'{i}-> {libro.titulo}    |       {libro.genero} | {libro.isbn}  |  {libro.editorial}  | {libro.autor}')
        print("---------------------------------------------------------------------------------------")
    print("=======================================================================================")
    return list_libros

def buscar_por_n_autores(list_libros: list[Libro],nro_autor: int) -> Libro:
    libros_encontrados =[]
    for l in list_libros:
        if type(l.autor) == type([]):
            if len(l.autor) == nro_autor:
                libros_encontrados.append(l)
        else:
            if nro_autor == 1:
                libros_encontrados.append(l)
    return libros_encontrados
                
                

def buscar_por_isbn(isbn: str, list_libros: list[Libro]) -> Libro:
    for l in list_libros:
        if isbn.strip()== l.isbn:
            return l
    return None

def ord_por_titulo(list_libros : list[Libro]) -> list:
    ordenado = sorted(list_libros,key=lambda a : a.titulo)
    return ordenado

def buscar_por_titulo(titulo: str, list_libros: list[Libro]) -> Libro:
    for l in list_libros:
        if titulo.strip()== l.titulo:
            return l
    return None

def opcion1() -> list[Libro]:
    print("Leyendo archivo libros.csv...")
    lista_libros = abrir_archivo(file='libros.csv')
    return lista_libros

#solicita una opcion 1 o 2  y retorna un libro resultado de la busqueda
def opcion5(lista_libros: list[Libro]) -> Libro:
    libro1 : Libro
    opcion = 0
    while opcion not in (1,2):
        print("1.  Buscar por titulo")
        print("2.  Buscar por ISBN")
        print("Ingrese 1 o 2 ")
        opcion = pedirNumeroEntero()

    if opcion == 1:
        titulo = input("Ingrese el titulo a buscar :")
        libro1 = buscar_por_titulo(titulo,lista_libros)
        return libro1

    elif opcion == 2:
        isbn = input("Ingrese el ISBN a buscar:")
        libro1 = buscar_por_isbn(isbn,lista_libros)
        return libro1
    else: 
        return None
def opcion8(lista_libros: list[Libro])-> list[Libro]:
    libros_encontrados = []
    opcion = 0
    while opcion not in range(1,10):
        print("Ingrese el numero de autores del libro que desea buscar: ")
        opcion = pedirNumeroEntero()
        libros_encontrados = buscar_por_n_autores(lista_libros,opcion)
        return libros_encontrados

    
def actualizar_libro(lista_libro: list[Libro], posicion: int,id,titulo,genero,isbn,editorial,autor) -> list[Libro]:
    lista_libro[posicion-1].id =id 
    lista_libro[posicion-1].titulo =titulo
    lista_libro[posicion-1].genero= genero
    lista_libro[posicion-1].isbn = isbn
    lista_libro[posicion-1].editorial = editorial
    lista_libro[posicion-1].autor = autor
    return lista_libro

def opcion9(lista_libros : list[Libro]) -> list[Libro]:
    print("Por favor ingrese una posicion valida (numero) del libro a editar o 0 para salir:")
    opcion = 0
    while opcion not in range(1,len(lista_libros)+1):
        opcion = pedirNumeroEntero() 
        if opcion in range(1,len(lista_libros)+1):
            id = input("Ingrese nuevo id: ")
            titulo=input("Ingrese nuevo titulo: ")
            genero=input("Ingrese nuevo genero: ")
            isbn=input("Ingrese nuevo isbn: ")
            editorial=input("Ingrese nuevo editorial: ")
            autor=input("Ingrese nuevo autor (si son mas de uno separalo con comas): ")
            lista = []
            autor = autor.strip()
            for a in autor.split(sep=","):
                lista.append(a.strip())
            if len(lista) >1:
                autor=lista  
            return actualizar_libro(lista_libros,opcion,id,titulo,genero,isbn,editorial,autor)
        elif opcion == 0:
            break
        else:
            print("Ingrese un numero valido o 0 para salir")




























#pide un numero entero al usuario y valida si es entero
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
        print("5.  Buscar libro por ISBN o titulo") 
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
    lista_libros=[]
    while True:
        opcion = menu_principal()
        if opcion == 1:
            os.system('cls')
            print ("Opcion 1")
            lista_libros = opcion1() 
            print(f"cantidad de libros cargados: {len(lista_libros)}")
            os.system('pause')
        elif opcion == 2:
            os.system('cls')
            print ("Opcion 2")
            listar_libros(lista_libros)
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
            libro = opcion5(lista_libros)
            if libro == None:
                print("No se encontraron coincidencias")
            else:
                print("Resultados :")
                print(f'{libro.titulo}    |    {libro.genero} | {libro.isbn}  |  {libro.editorial}  | {libro.autor}')
            os.system('pause')
        elif opcion == 6:
            os.system('cls')
            print("Opcion 6")
            lista_libros = ord_por_titulo(lista_libros)
            print("Lista ordenada")
            listar_libros(lista_libros)
            os.system('pause')
        elif opcion == 7:
            os.system('cls')
            print("Opcion 7")
            os.system('pause')
        elif opcion == 8:
            os.system('cls')
            print("Opcion 8")
            resultado = opcion8(lista_libros)
            if len(resultado) <1:
                print("No se encontraron resultados")
            else:
                print("Resultados")
                listar_libros(resultado)
            os.system('pause')
        elif opcion == 9:
            os.system('cls')
            print("Opcion 9")
            if len(lista_libros) == 0:
                print("No hay datos para actualizar, aniada libros ")
            else:
                print("Actualizar libro")
                listar_libros(lista_libros)
                lista_libros = opcion9(lista_libros)
                print("Lista Actualizada")
                listar_libros(lista_libros)
            os.system('pause')
        elif opcion == 10:
            os.system('cls')
            print("Opcion 10")
            try:
                if len(lista_libros) == 0:
                    print("No hay datos para guardar, aniada libros ")
                else:
                    escribir_archivo(lista_libros)
                    
            except Exception as ex:
                print(ex)
            os.system('pause') 
        elif opcion == 11:
            print("SALIR")
            break       
        else:
            os.system('cls')
            print("Ingresa un nuevo numero :")
        
    
if __name__ == '__main__':
    main()
    # a1 = Libro("001","ABCtitulo","comedia","00123","santillana")
    # a1.autor = 'autor,autor2,auto3'
    # print(a1.autor)