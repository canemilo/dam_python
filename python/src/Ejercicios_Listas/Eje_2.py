from Eje_1 import pokemons



sumatorio = 0
numero_pokemons = len(pokemons)

for pokemon in pokemons:
    sumatorio += pokemon["altura_m"]

    media = sumatorio / numero_pokemons
    print("La media de altura de los Pokémon es:", round(media,2)," metros")


