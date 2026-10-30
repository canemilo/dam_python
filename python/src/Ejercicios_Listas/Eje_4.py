from Eje_1 import pokemons

es_agua = False

for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if tipo == 'Agua':
            print(pokemon["nombre"], pokemon["tipos"])
            break




