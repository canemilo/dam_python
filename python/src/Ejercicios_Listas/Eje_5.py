from Eje_1 import pokemons

print("Pokemons cuyos tipos terminan en 'a':")


for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        # Comprobamos si la variable 'tipo' termina en 'a'
        if tipo.endswith('a'): 
            print(pokemon["nombre"], pokemon["tipos"])
            break 
