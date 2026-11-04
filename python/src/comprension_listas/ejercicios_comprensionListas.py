"""
Introducción al uso de Python
Ejercicios de comprensión de listas
"""

from pprint import pprint

# ---------------------------------------------------------------------------
# Anexo I
# ---------------------------------------------------------------------------
jugadores = [
    {
        "nombre": "Lionel Messi",
        "equipo": "Inter Miami",
        "dorsal": 10,
        "atributos": {"tiro": 10, "pase": 10, "regate": 10},
        "filigranas": ["ruleta", "caño", "sombrero", "bicicleta"],
    },
    {
        "nombre": "Vinicius Jr",
        "equipo": "Real Madrid",
        "dorsal": 7,
        "atributos": {"tiro": 8, "pase": 7, "regate": 9},
        "filigranas": ["elasticidad", "bicicleta", "ruleta"],
    },
    {
        "nombre": "Pedri",
        "equipo": "FC Barcelona",
        "dorsal": 8,
        "atributos": {"tiro": 6, "pase": 9, "regate": 8},
        "filigranas": ["ruleta", "caño"],
    },
    {
        "nombre": "Lamine Yamal",
        "equipo": "FC Barcelona",
        "dorsal": 19,
        "atributos": {"tiro": 8, "pase": 8, "regate": 9},
        "filigranas": ["bicicleta", "elasticidad"],
    },
    {
        "nombre": "Luka Modric",
        "equipo": "Real Madrid",
        "dorsal": 10,
        "atributos": {"tiro": 7, "pase": 10, "regate": 8},
        "filigranas": ["exterior", "ruleta"],
    },
    {
        "nombre": "Erling Haaland",
        "equipo": "Manchester City",
        "dorsal": 9,
        "atributos": {"tiro": 10, "pase": 5, "regate": 6},
        "filigranas": ["sombrero"],
    },
]


def titulo(n, texto):
    print(f"\n--- Ejercicio {n}: {texto} ---")


# 1. Lista solo con los nombres de todos los futbolistas
nombres = [j["nombre"] for j in jugadores]
titulo(1, "Nombres de todos los futbolistas")
print(nombres)

# 2. Jugadores que llevan el dorsal número 10
dorsal_10 = [j for j in jugadores if j["dorsal"] == 10]
titulo(2, "Jugadores con el dorsal 10")
pprint(dorsal_10, sort_dicts=False)

# 3. Nombres de los jugadores del "FC Barcelona"
barcelona = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]
titulo(3, "Jugadores del FC Barcelona")
print(barcelona)

# 4. Nombres de los jugadores con pase >= 9
buenos_pasadores = [j["nombre"] for j in jugadores if j["atributos"]["pase"] >= 9]
titulo(4, "Jugadores con pase >= 9")
print(buenos_pasadores)

# 5. Jugadores que saben hacer la filigrana "ruleta"
hacen_ruleta = [j for j in jugadores if "ruleta" in j["filigranas"]]
titulo(5, "Jugadores que saben hacer la ruleta")
pprint(hacen_ruleta, sort_dicts=False)

# 6. Jugadores con tiro >= 8 Y regate >= 9
tiro_y_regate = [
    j for j in jugadores
    if j["atributos"]["tiro"] >= 8 and j["atributos"]["regate"] >= 9
]
titulo(6, "Jugadores con tiro >= 8 y regate >= 9")
pprint(tiro_y_regate, sort_dicts=False)

# 7. Cadenas con la forma "Nombre (Equipo)"
nombre_equipo = [f"{j['nombre']} ({j['equipo']})" for j in jugadores]
titulo(7, "Nombre (Equipo)")
print(nombre_equipo)

# 8. Tuplas (nombre, "Goleador" si tiro >= 9, si no "Asistente")
roles = [
    (j["nombre"], "Goleador" if j["atributos"]["tiro"] >= 9 else "Asistente")
    for j in jugadores
]
titulo(8, "Goleador o Asistente")
print(roles)

# 9. Nombres de los jugadores que dominan más de 2 filigranas distintas
#    (se usa set() para contar solo las filigranas distintas)
mas_de_2_filigranas = [j["nombre"] for j in jugadores if len(set(j["filigranas"])) > 2]
titulo(9, "Jugadores con más de 2 filigranas distintas")
print(mas_de_2_filigranas)

# 10. Todas las filigranas de todos los jugadores en una única lista
#     (comprensión anidada: primero se recorre cada jugador, luego cada filigrana)
todas_filigranas = [f for j in jugadores for f in j["filigranas"]]
titulo(10, "Todas las filigranas")
print(todas_filigranas)