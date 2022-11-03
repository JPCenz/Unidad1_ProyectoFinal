import time,requests
def mostrar_mensaje_espera(segundos=5):
    #importar libreria time
    print("Espere mientras se obtiene la informacion del servidor")
    for i in range(segundos):        
        print(" -- ",end=" ",flush=True)
        time.sleep(1)
    print("")

def buscar_por_forma(forma):
    try:
        mostrar_mensaje_espera(3)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon-form/{forma}')
        res.raise_for_status()
        data = res.json()
        imagen = data['sprites']["front_default"]
        url_pokemon = data['pokemon']['url']
        contador = 0
        res1 = requests.get(url_pokemon)
        res1.raise_for_status()
        data1= res1.json()
        nombre : str = data1['name']
        habilidades= []
        imagen : str 
        for i in data1['abilities']:
            habilidades.append(i['ability']['name'])
        contador = contador + 1       
        # print("----------------------------------------------------------------------------------")
        print(f"{contador}.  POKE: {nombre.capitalize()}, Habilidades: {','.join(habilidades)}, Imagen: {imagen}")
        print("-------------------------------------------------------------------------------------")        
    except requests.HTTPError as ex:
        print("Forma no encontrada")
        


def opcion2():
    print("Ejemplos de formas: luxio, luxray, metang, electrike, volbeat, carvanha,voltorb")
    a = input("Ingrese una forma de pokemon a buscar:").lower()
    try:
        buscar_por_forma(a)
    except Exception as ex:
        print(ex)
    input("Presione enter para continuar")

opcion2()