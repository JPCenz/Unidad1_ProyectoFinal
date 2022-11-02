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

def opcion3():
    try:
        url = 'https://pokeapi.co/api/v2/ability/'
        response = requests.get(url)
        data0 = response.json()
        habilidades = []
        url_habilidades = []
        for i in data0['results']:
            habilidades.append(i['name'])
            url_habilidades.append(i['url'])
        k = 1
        for i in habilidades:
            print(f'Habilidad {k}: {i}')
            k +=1
        while True:
            valor = input("\nINGRESE UN NUMERO DE HABILIDAD\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                    for i in range(1,21):
                        if valor == i:
                            url1 = f'https://pokeapi.co/api/v2/ability/{valor}'
                            lista_pokemon = []
                            habilidades_pokemon = []
                            url_imagenpokemon = []
                            
                            response1 = requests.get(url1)
                            data1 = response1.json()['pokemon']
                            lista = []
                            url_pokemon = []
                            for j in data1:
                                lista.append(j)
                            
                            for k in range (len(data1)):
                                lista_pokemon.append(lista[k]['pokemon']['name'])
                                url_pokemon.append(lista[k]['pokemon']['url'])
                            
                            for l in url_pokemon:
                                lista_habilidades = []
                                respons = requests.get(l)
                                data2 = respons.json()['abilities']
                                data3 = respons.json()['sprites']['front_default']
                                url_imagenpokemon.append(data3)
                                for m in data2:
                                    lista_habilidades.append(m['ability']['name'])
                                habilidades_pokemon.append(lista_habilidades)
                            
                            print(f"\nLista de pokemones con la habilidad {valor} son:\n")
                            for count, (i,j,k) in enumerate(zip(lista_pokemon,habilidades_pokemon,url_imagenpokemon), start=1):
                                print(f'{count}> Pokemon: {i} >Habilidades: {j} >Url_img: {k}')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-20]: ')
            else:
                print('Ingrese una habilidad aceptable [1-20]: ')
    except Exception as ex:
        print(ex)


def opcion4():
    try:
        url = 'https://pokeapi.co/api/v2/pokemon-habitat/'
        response = requests.get(url)
        data0 = response.json()
        habitad = []
        url_habitad = []
        for i in data0['results']:
            habitad.append(i['name'])
            url_habitad.append(i['url'])
        k = 1
        for i in habitad:
            print(f'Habitad {k}: {i}')
            k +=1
        while True:
            valor = input("\nINGRESE UN NUMERO DE HABITAD\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in [1,2,3,4,5,6,7,8,9]:
                    for i in range(1,10):
                        if valor == i:
                            url1 = f'https://pokeapi.co/api/v2/pokemon-habitat/{valor}/'
                            lista_pokemon = []
                            habilidades_pokemon = []
                            url_imagenpokemon = []
                            
                            response1 = requests.get(url1)
                            data1 = response1.json()['pokemon_species']
                            url_pokemon = []
                            for j in data1:
                                lista_pokemon.append(j['name'])
                                url_pokemon.append(j['url'])

                            url_data_pokemons = []
                            for k in url_pokemon:
                                response2 = requests.get(k)
                                data2 = response2.json()['varieties'][0]['pokemon']
                                url_data_pokemons.append(data2['url'])
                            
                            for l in url_data_pokemons:
                                habilidades_temporal = []
                                response3 = requests.get(l)
                                data3 = response3.json()['abilities']
                                data4 = response3.json()['sprites']['front_default']
                                url_imagenpokemon.append(data4)
                                for m in data3:
                                    habilidades_temporal.append(m['ability']['name'])
                                habilidades_pokemon.append(habilidades_temporal)
                          
                            print(f"\nLa lista de pokemones con la Habitad {valor} son:\n")
                            for count, (i,j,k) in enumerate(zip(lista_pokemon,habilidades_pokemon,url_imagenpokemon), start=1):
                                print(f'{count}> Pokemon: {i} >Habilidades: {j} >Url_img: {k}')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-9]: ')
            else:
                print('Ingrese una habilidad aceptable [1-9]: ')
    except Exception as ex:
        print(ex)


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
            opcion3()
            os.system('pause')
        elif opcion == 4:
            os.system('cls')
            print("Opcion 4")
            opcion4()
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