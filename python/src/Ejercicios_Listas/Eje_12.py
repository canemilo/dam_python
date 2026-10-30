from Eje_8 import personajes_frieren

for personaje in personajes_frieren[:]: ## COPIA PARA ITERAR Y ELIMINAR
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)

for personaje in personajes_frieren:
    print(personaje["nombre"], personaje["raza"])

    