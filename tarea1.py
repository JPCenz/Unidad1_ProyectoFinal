import csv
from dataclasses import field

class Libro():
    id = 0
    titulo = ""
    genero = ""
    ISBN = ""
    editorial = ""
    autor = []

def opcion1(librox):
    
    with open (librox, 'r') as read_book:
        leer = csv.reader(read_book)
        for i in leer:
            print(i)

def opcion2(lilibro):
    with open (lilibro, 'r') as lista_book:
        leer = csv.reader(lista_book)
        for i in leer:
            print(i[0])

# def opcion3(addlibro):
#     field_name = ['Libro','Id','Titulo','Genero','ISBN','Editorial','Autor']
#     dict = {"Libro":"libro4","Id": "444","Titulo": "titulo4","Genero": "genero4", "ISBN":"444-44-44444-44-4", "Editorial":"editorial4","Autor":"autor4"}
#     with open (addlibro, 'a') as agre_book:
#         dict_object = csv.DictWriter(agre_book, fieldnames=field_name)
#         dict_object.writerow(dict)
#         with open(agre_book, 'r') as read_agre_book:
#             lineas = read_agre_book.read().splitlines()
            # print(lineas)
opcion1(librox='libros.csv')
opcion2(lilibro='libros.csv')
# opcion3(addlibro='libros.csv')