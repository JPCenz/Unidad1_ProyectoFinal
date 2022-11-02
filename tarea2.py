import os, requests

def opcion1():

    while True:
        n = input('Ingrese numero de generacion [1-8]: ')
        if n.isnumeric():
            n=int(n)
            if n in [1,2,3,4,5,6,7,8]:
                if n == 1:
                    n_gen = "i"
                elif n == 2:
                    n_gen = "ii"
                elif n == 3:
                    n_gen = "iii"
                elif n == 4:
                    n_gen = "iv"
                elif n == 5:
                    n_gen = "v"
                elif n == 6:
                    n_gen = "vi"
                elif n == 7:
                    n_gen = "vii"
                else:
                    n_gen = "viii"
                
                try:
                    url = f'https://pokeapi.co/api/v2/generation/{n}'
                    lista_poke = []
                    habi_poke = []
                    URL_poke = []
                    lista_url = []
                    response = requests.get(url)

                    # LISTA DE POKEMONES:
                    data = response.json()['pokemon_species']
                    for i in data:
                        lista_poke.append(i['name'])
                        lista_url.append(i['url'])

                    for j in lista_url:
                        habilidad = []
                        link = []
                        respo = requests.get(j)
                        url1 = respo.json()['varieties'][0]['pokemon']['url']

                        response1 = requests.get(url1)
                        dataj = response1.json()['abilities']
                        datak = response1.json()['sprites']['versions'][f'generation-{n_gen}']
                        for k in dataj:
                            habilidad.append(k['ability']['name'])
                        habi_poke.append(habilidad)
                        for l in datak:
                            link.append(datak[l]['front_default'])
                        URL_poke.append(link)

                    for count, (i,j,k) in enumerate(zip(lista_poke,habi_poke,URL_poke)):
                        print(f'POKE: {i} HABILIDAD: {j} LINK: {k}')
                    break

                except Exception as ex:
                    print(ex)
            else:
                print('Ingrese una generacion aceptable [1-8]: ')
        else:
            print('Ingrese una generacion aceptable [1-8]: ')

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
    while opcion != range (1,7):
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
            opcion1()
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