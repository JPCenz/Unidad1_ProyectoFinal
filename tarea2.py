import time, requests
from os import system, name

def mostrar_mensaje_espera(segundos=5):
    #importar libreria time
    print("Espere mientras se obtiene la informacion del servidor")
    for i in range(segundos):      
        print(" -- ",end=" ",flush=True)
        time.sleep(1)
    print("")

def opcion1():
    try:
        mostrar_mensaje_espera(2)
        url0 = 'https://pokeapi.co/api/v2/generation/'
        response0 = requests.get(url0)
        data0 = response0.json()
        generaciones = []
        
        for f in data0['results']:
            generaciones.append(f['name'])
        # Se muestra la lista de generaciones de pokemons
        print(f'\nLISTA DE GENERACIONES POKEMONS.\n')
        for c, h in enumerate(generaciones, start=1):
            print(f'{c}: {h}')

        while True:
            valor = input("\nINGRESE UN NUMERO DE GENERACION\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in range(1,len(generaciones)+1):
                    count = 0
                    print(f"\nSe muestra lista de Pokemons de la generacion {valor}:\n")
                    for i in range(1,len(generaciones)+1):
                        if valor == i:
                            url1 = f'https://pokeapi.co/api/v2/generation/{valor}/'
                            response1 = requests.get(url1)
                            data1 = response1.json()['pokemon_species']
                            for j in data1:

                                # Se muestra el nombre del pokemon segun su generacion.
                                nombre_pokemon = j['name']
                                url_species_pokemon =j['url']

                                response2 = requests.get(url_species_pokemon)
                                data2 = response2.json()['varieties'][0]['pokemon']
                                url_datapokemon = data2['url']

                                # Se muestra url imagen del pokemon segun su generacion.
                                lista_habilidades = []
                                response3 = requests.get(url_datapokemon)
                                data3 = response3.json()['abilities']
                                url_imagenpokemon = response3.json()['sprites']['front_default']

                                # Se muestra las habilidades del pokemon segun su generacion.
                                for m in data3:
                                    lista_habilidades.append(m['ability']['name'])

                                #se imprimen datos segun se va analizando informacion.
                                count += 1
                                print(f"{count}>> POKEMON: {nombre_pokemon}  ||  HABILIDADES: {','.join(lista_habilidades)}\n\tURL_IMAGEN: {url_imagenpokemon}")
                                print("---------------------------------------------------------------------------------------------------------")

                    print(f'\nLa lista de pokemones de la generacion {valor} contiene {count} pokemones.')                             
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-8]: ')
            else:
                print('Ingrese una habilidad aceptable [1-8]: ')

    except Exception as ex:
        print(ex)


def opcion2():
    try:
        mostrar_mensaje_espera(2)
        url0 = 'https://pokeapi.co/api/v2/pokemon-shape/'
        response0 = requests.get(url0)
        data0 = response0.json()
        formas = []
        for g in data0['results']:
            formas.append(g['name'])
        
        # Se muestra la lista de formas pokemons
        print(f'\nLISTA DE FORMAS POKEMONS.\n')
        for c, i in enumerate(formas, start=1):
            print(f'Forma {c}: {i}')
            
        while True:
            valor = input("\nINGRESE EL NUMERO DE LA FORMA\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in range(1,len(formas)+1):
                    count = 0
                    print(f"\nSe muestra lista de pokemons de la forma {valor}:\n")
                    for i in range(1,len(formas)+1):
                        if valor == i:
                            url1 = f'{url0}{valor}/'                          
                            response1 = requests.get(url1)
                            data1 = response1.json()['pokemon_species']
                            for j in data1:
                                # Se muestra el nombre del pokemon segun su forma.
                                nombre_pokemon = j['name']
                                url_species_pokemon = j['url']

                                response2 = requests.get(url_species_pokemon)
                                data2 = response2.json()['varieties'][0]['pokemon']
                                url_datapokemon = data2['url']

                                # Se muestra url imagen del pokemon segun su forma.
                                lista_habilidades = []
                                response3 = requests.get(url_datapokemon)
                                data3 = response3.json()['abilities']
                                url_imagenpokemon = response3.json()['sprites']['front_default']

                                # Se muestra las habilidades del pokemon segun su forma.
                                for o in data3:
                                    lista_habilidades.append(o['ability']['name'])

                                #se imprimen datos segun se va analizando informacion.
                                count += 1
                                print(f"{count}>> POKEMON: {nombre_pokemon}  ||  HABILIDADES: {','.join(lista_habilidades)}\n\tURL_IMAGEN: {url_imagenpokemon}")
                                print("---------------------------------------------------------------------------------------------------------")

                    print(f'\nLa lista de pokemones de forma {valor} contiene {count} pokemones.')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-14]: ')
            else:
                print('Ingrese una habilidad aceptable [1-14]: ')
    except Exception as ex:
        print(ex)


def opcion3():
    try:
        mostrar_mensaje_espera(2)
        url = 'https://pokeapi.co/api/v2/ability/'
        response0 = requests.get(url)
        data0 = response0.json()
        habilidades = []
        for g in data0['results']:
            habilidades.append(g['name'])

        # Se muestra la lista de habilidades pokemons
        print(f'\nLISTA DE HABILIDADES POKEMONS.\n')
        for c, h in enumerate(habilidades, start=1):
            print(f'Habilidad {c}: {h}')

        while True:
            valor = input("\nINGRESE UN NUMERO DE HABILIDAD\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in range(1,len(habilidades)+1):
                    count = 0
                    print(f"\nSe muestra lista de pokemons de la habilidad {valor}:\n")
                    for i in range(1,len(habilidades)+1):
                        if valor == i:
                            url1 = f'{url}{valor}/'                          
                            response1 = requests.get(url1)
                            data1 = response1.json()
                            for j in data1['pokemon']:
                                # Se muestra el nombre del pokemon segun su habilidad.
                                nombre_pokemon = j['pokemon']['name']
                                url_datapokemon = j['pokemon']['url']

                                # Se muestra url imagen del pokemon segun su habilidad.
                                lista_habilidades = []
                                response2 = requests.get(url_datapokemon)
                                data2 = response2.json()['abilities']
                                url_imagenpokemon = response2.json()['sprites']['front_default']

                                # Se muestra las habilidades del pokemon segun su habilidad.
                                for k in data2:
                                    lista_habilidades.append(k['ability']['name'])

                                #se imprimen datos segun se va analizando informacion.
                                count += 1
                                print(f"{count}>> POKEMON: {nombre_pokemon}  ||  HABILIDADES: {','.join(lista_habilidades)}\n\tURL_IMAGEN: {url_imagenpokemon}")
                                print("---------------------------------------------------------------------------------------------------------")
                                
                    print(f'\nLa lista de pokemones con la habilidad {valor} contiene {count} pokemones.')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-20]: ')
            else:
                print('Ingrese una habilidad aceptable [1-20]: ')
    except Exception as ex:
        print(ex)


def opcion4():
    try:
        mostrar_mensaje_espera(2)
        url0 = 'https://pokeapi.co/api/v2/pokemon-habitat/'
        response0 = requests.get(url0)
        data0 = response0.json()
        habitad = []

        for g in data0['results']:
            habitad.append(g['name'])

        # Se muestra la lista de habitads pokemons
        print(f"\nLISTA DE HABITAD'S POKEMONS.\n")
        for c, h in enumerate(habitad, start=1):
            print(f'Habitad {c}: {h}')

        while True:
            valor = input("\nINGRESE UN NUMERO DE HABITAD\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in range(1,len(habitad)+1):
                    count = 0
                    print(f"\nSe muestra lista de pokemons del habitad {valor}:\n")
                    for i in range(1,len(habitad)+1):
                        if valor == i:
                            url1 = f'{url0}{valor}/'                            
                            response1 = requests.get(url1)
                            data1 = response1.json()['pokemon_species']
                            url_pokemon = []
                            for j in data1:
                                # Se muestra el nombre del pokemon segun su habitad.
                                nombre_pokemon = j['name']
                                url_pokemon = j['url']

                                response2 = requests.get(url_pokemon)
                                data2 = response2.json()['varieties'][0]['pokemon']
                                url_datapokemon = data2['url']

                                # Se muestra url imagen del pokemon segun su habitad.
                                lista_habilidades = []
                                response3 = requests.get(url_datapokemon)
                                data3 = response3.json()['abilities']
                                url_imagenpokemon = response3.json()['sprites']['front_default']

                                # Se muestra las habilidades del pokemon segun su habitad.
                                for k in data3:
                                    lista_habilidades.append(k['ability']['name'])

                                #se imprimen datos segun se va analizando informacion.
                                count += 1
                                print(f"{count}>> POKEMON: {nombre_pokemon}  ||  HABILIDADES: {','.join(lista_habilidades)}\n\tURL_IMAGEN: {url_imagenpokemon}")
                                print("---------------------------------------------------------------------------------------------------------")
                                
                    print(f'\nLa lista de pokemones con la habilidad {valor} contiene {count} pokemones.')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-9]: ')
            else:
                print('Ingrese una habilidad aceptable [1-9]: ')
    except Exception as ex:
        print(ex)

def opcion5():
    try:
        mostrar_mensaje_espera(2)
        url0 = 'https://pokeapi.co/api/v2/type/'
        response = requests.get(url0)
        data0 = response.json()
        tipo = []

        for g in data0['results']:
            tipo.append(g['name'])

        # Se muestra la lista de tipos de pokemons
        print(f"\nLISTA DE TIPOS POKEMONS.\n")
        for c, h in enumerate(tipo, start=1):
            print(f'Tipo {c}: {h}')

        while True:
            valor = input("\nINGRESE UN NUMERO DE LA LISTA TIPO\nValor: ")
            if valor.isnumeric():
                valor = int(valor)
                if valor in range(1,len(tipo)+1):
                    count = 0
                    print(f'\nSe muestra lista de pokemons del tipo {valor}:\n')
                    for i in range(1,len(tipo)+1):
                        if valor == i:
                            if valor == 20:
                                valor = 10002
                                print('No hay pokemones con la forma 20.')
                                break
                            if valor == 19:
                                valor = 10001
                                print('No hay pokemones con la forma 19.')
                                break

                            url1 = f'{url0}{valor}/'                           
                            response1 = requests.get(url1)
                            data1 = response1.json()
                            for j in data1['pokemon']:
                                # Se muestra el nombre del pokemon segun su tipo.
                                nombre_pokemon = j['pokemon']['name']
                                url_datapokemon = j['pokemon']['url']

                                # Se muestra url imagen del pokemon segun su tipo.
                                lista_habilidades = []
                                response2 = requests.get(url_datapokemon)
                                data2 = response2.json()['abilities']
                                url_imagenpokemon = response2.json()['sprites']['front_default']

                                # Se muestra las habilidades del pokemon segun su tipo.
                                for k in data2:
                                    lista_habilidades.append(k['ability']['name'])

                                #se imprimen datos segun se va analizando informacion.
                                count += 1
                                print(f"{count}>>  POKEMON: {nombre_pokemon} ||  HABILIDADES: {', '.join(lista_habilidades)}\n\tURL_IMAGEN: {url_imagenpokemon}")
                                print("------------------------------------------------------------------------------------------------------")

                    print(f'\nLa lista de pokemones del tipo {i} contiene {count} pokemones.\n')
                    break
                else:
                    print('Ingrese una habilidad aceptable [1-20]: ')
            else:
                print('Ingrese una habilidad aceptable [1-20]: ')
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
        print('\n================= TAREA 2 ===================')
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
    def clear():
        if name == 'nt': 
            x = system('cls') 
        else: 
            x = system('clear')

    def pause():
        if name == 'nt':
            print("\nPresione una tecla para continuar ...")
            y = system('pause')
        else:
            y = system("""bash -c 'read -s -n 1 -p "\nPresione una tecla para continuar ..."'""")
            clear()

    while True:
        opcion = menu_principal()
        if opcion == 1:
            clear()
            print ("Opcion 1")
            opcion1()
            pause()
        elif opcion == 2:
            clear()
            print ("Opcion 2")
            opcion2()
            pause()
        elif opcion == 3:
            clear()
            print("Opcion 3")
            opcion3()
            pause()
        elif opcion == 4:
            clear()
            print("Opcion 4")
            opcion4()
            pause()
        elif opcion == 5:
            clear()
            print("Opcion 5")
            opcion5()
            pause()
        elif opcion == 6:
            print("SALIR")
            break       
        else:
            clear()
            print("\nIngresa un nuevo numero :")
    
if __name__ == '__main__':
    main()