from Eje_8 import personajes_frieren

print('Magos de Primera Clase')
for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Magos de Primera Clase":
            print(personaje["nombre"], personaje["raza"])
            break