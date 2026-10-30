from Eje_1 import pokemons


print('Insertar un nuevo POKEMON al final de la lista de pokemons')

pokemons.append({'nombre': 'Meow', "generacion": 1,
                "categoria": "ladron",
                  "tipos": ["normal", "gato"],
                  "peso_kg": 7,
                  "altura_m": 0.45
    })

for pokemon in pokemons:
    print(pokemon)


