from Eje_8 import personajes_frieren


print('Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python')


for personaje in personajes_frieren:
    if personaje["raza"] == "Elfo":
        personaje["afiliacion"].append("Elfos Supervivientes del Examen de Python")

for personaje in personajes_frieren:
    print(personaje["nombre"], personaje["raza"], personaje["afiliacion"])
    