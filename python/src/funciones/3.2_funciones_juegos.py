"""
Dada la lista de videojuegos dispuesta más abajo, crea una función llamada comprobar_stock que reciba el nombre de un juego y devuelva los siguientes valores tras comprobar las unidades disponibles:
Si las unidades son 0, devuelve "Agotado".
Si las unidades son mayores que 0 y menores o iguales que 10, devuelve "Últimas unidades".
Si las unidades son mayores que 10 y menores o iguales que 50, devuelve "Stock normal".
Si las unidades son mayores que 50, devuelve "Exceso de stock".
Si el juego no existe en la lista, lanza una excepción con raise ValueError.
Debe dar igual si el usuario escribe el nombre en mayúsculas o minúsculas.


"""
juegos = [
    ["Elden Ring", "RPG", 45],
    ["Hollow Knight", "Metroidvania", 0],
    ["FIFA 26", "Deportes", 120],
    ["The Witcher 3", "RPG", 8]
]
print(f"------  USANDO LISTAS EN EL METODO --------")
def comprobar_stock(nombre):
    for titulo,genero,stock in juegos:
        if nombre.lower() == titulo.lower():
            if stock == 0:
                return "Agotado"
            elif stock <= 10:
                return "Ultimas unidades"
            elif stock <= 50:
                return "Stock normal"
            else:
                return "Exceso de stock"
            
    raise ValueError(f"El juego '{nombre}' no esta en la lista")


'''pruebas'''
# --- PRUEBAS ---
print(f" --- PRUEBAS ---")
      
print(comprobar_stock("Elden ring"))
print(comprobar_stock("Fifa 26"))
print(comprobar_stock("The witcher 3"))

print(f"ERRORES capturados")
try:
    print(comprobar_stock("fifa 27"))
except ValueError as e:
    print("Error capturado:", e)
    
print()
print()
print(f"------  USANDO Diccionarios EN EL METODO --------")


juegos_dicc = {titulo.lower(): {"genero": genero, "stock": stock} for titulo, genero, stock in juegos}

def comprobar_stock_diccionario(nombre):
    clave = nombre.lower()
    
    # 1. Comprobar si existe
    if clave not in juegos_dicc:
        raise ValueError(f"El juego '{nombre}' no está en la lista")
    
    # 2. Acceso directo al stock por su nombre sin bucles ni índices
    stock = juegos_dicc[clave]["stock"]
    
    if stock == 0:
        return "Agotado"
    elif stock <= 10:
        return "Últimas unidades"
    elif stock <= 50:
        return "Stock normal"
    else:
        return "Exceso de stock"

# --- PRUEBAS ---
print(comprobar_stock_diccionario("fifa 26"))     # Exceso de stock
print(comprobar_stock_diccionario("Elden Ring"))  # Stock normal

# Si quieres probar el caso sin espacio ("fifa26"), envuélvelo en try/except:
try:
    print(comprobar_stock_diccionario("fifa26"))
except ValueError as e:
    print("Error capturado:", e)
