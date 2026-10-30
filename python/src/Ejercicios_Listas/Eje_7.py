from Eje_1 import pokemons

print('Eliminar todos los POKEMON de tipo = normal de la lista')
for pokemon in pokemons:
    print(pokemon)
print('--------------------')

# El truco está en el [:] para iterar sobre una copia
for pokemon in pokemons[:]:
    for tipo in pokemon["tipos"]:
        if tipo == "Normal":
            pokemons.remove(pokemon)
            break  # Detiene la revisión de tipos de este pokemon y pasa al siguiente

print('LISTA DE POKEMONS UNA VEZ BORRADOS TODOS LOS POKEMONS DE TIPO NORMAL')
for pokemon in pokemons:
    print(pokemon)
print('--------------------')
