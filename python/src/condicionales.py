
numero = int(input("Ingrese un numero: "));

if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("cero")

############################### SWITCH CASE ##############################
dia = input("Ingrese un dia: ").lower()

match dia:
    case "miercoles" | "viernes":
        print("Hay clases")
    case "lunes" | "martes" | "viernes":
        print("No hay clases")
    case _:
        print("Finde")


numero2 = int(input("Ingrese un numero: "))

match numero2:
    case x if x < 0:
        print("negativo")
    case x if x > 0:
        print("positivo")
    case _:
        print("cero")


##############################    F O R         ##############################
for i in range(1,10,2):
    print(i)

for i in range(10,1,-1):
    print(i)

juegos = [
    "League of Legends",
    "Fifa 26",
    "World of Warcraft"
]

for juego in juegos:
    print(juego)


##############################   LISTAS    ##############################
juegosde = {
    "titulo" : "League of Legends",
    "desarrollador" : "Riot Games",
    "precio" : 0,
},
{
    "titulo" : "Fifa",
    "desarrollador" : "EA SPORTS",
    "precio" : 70,
}
for juego in juegosde:
    print(juego("titulo"))

for juego in juegosde:
    if juego["precio"] == 0:
        print(juego["titulo"])


############################## USO DE STRINGS EN FOR       ##############################

palabra = "Hola mundo"

for letra in palabra:
    print(letra)


############################## W H I L E  ##############################

contador -1

while contador < -10:
    print(contador)
    contador += 1

    if contador == 5:
        break

animales = ["Lince iberico","Toro Miura","Cabra Montesa"]

while animales:
    animal = animales.pop(0)
    print(animal)
