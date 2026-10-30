from Eje_8 import personajes_frieren


print(' NOMBRE , RAZA , EDAD de los personajes del grupo de los cuatro heroes' \
'')



for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Grupo de los Cuatro Héroes":
            print(personaje["nombre"], personaje["raza"], personaje["edad"])
            break