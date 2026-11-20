animales = [
    ["Lobo ibérico", "Mamífero", 2500],
    ["Lince ibérico", "Mamífero", 1668],
    ["Quebrantahuesos", "Ave", 2000],
    ["Oso pardo", "Mamífero", 500]
]

# CREAR DICCIONARIO
animales_dic = {nombre.lower(): {"especie": especie, "ejemplares": ejemplares} for nombre, especie, ejemplares in animales}


def comprobar_estado(nombre):
    clave = nombre.lower()

    # 1. Comprobar si existe
    if clave not in animales_dic:
        raise ValueError(f"El nombre '{nombre}' no está en la lista")

    # 2. Acceso directo a los ejemplares 
    ejemplares = animales_dic[clave]["ejemplares"]

    # 3. Evaluar estado
    if ejemplares < 1000:
        return "En peligro crítico"
    elif ejemplares <= 2000:
        return "En peligro"
    else:
        return "Estable"


# --- PRUEBAS ---
print(comprobar_estado("Oso pardo"))       # En peligro crítico
print(comprobar_estado("LINCE IBÉRICO"))   # En peligro
print(comprobar_estado("Lobo ibérico"))    # Estable

########### COMPROBAR ERROR CON TRY: #############
try:
    print(comprobar_estado("Águila imperial"))
except ValueError as e:
    print("Error capturado:", e)