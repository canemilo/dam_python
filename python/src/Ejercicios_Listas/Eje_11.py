from Eje_8 import personajes_frieren


print('Inserta al final de la lista de personajes un nuevo personaje con los siguientes datos: nombre: "Frey", raza: "Elfo", edad: 1000, afiliacion: ["Magos de Primera Clase", "Elfos del Bosque"]')

personajes_frieren.append({
    "nombre": "Frey",
    "raza": "Elfo",
    "clase":" Mago",
    "edad":44,
    "afiliacion": ["Magos de Primera Clase", "Elfos del Bosque"]
})


for personaje in personajes_frieren:
    print(personaje)



