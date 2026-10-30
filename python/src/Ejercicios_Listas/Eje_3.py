from Eje_1 import pokemons
from Eje_2 import media

for pokemon in pokemons:
    if pokemon["altura_m"] < media:
        print(f'{pokemon["nombre"]}: {pokemon["altura_m"]} m')