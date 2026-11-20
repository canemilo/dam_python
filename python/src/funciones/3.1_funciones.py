'''
2. Dada la lista de animales dispuesta más abajo, crea una función
comprobar_estado, que reciba el nombre de una especie y devuelva los
siguientes valores después de comprobar en la lista animales el número de
ejemplares que tiene:
● Si el número de ejemplares es 0, “Extinto”
● Si el número de ejemplares es mayor que 0 y menor o igual que 500, “En
peligro crítico”
● Si el número de ejemplares es mayor a 500 y menor o igual a 2000, “En
peligro”
● Si el número de ejemplares es mayor a 2000, “Amenazado”
● Si la especie no está en la lista, se lanzará una excepción con raise.
Será indiferente si el nombre de la especie está en mayúsculas o minúsculas.
animales = [
["Lobo ibérico", "Mamífero", 2500],
["Lince ibérico", "Mamífero", 1668],
["Quebrantahuesos", "Ave", 2000],
["Oso pardo", "Mamífero", 500]
'''


animales = [["Lobo ibérico", "Mamífero", 2500],
            ["Lince ibérico", "Mamífero", 1668],
            ["Quebrantahuesos", "Ave", 2000],
            ["Oso pardo", "Mamífero", 500]]


def comprobar_estado(especie):
    
    
    for nombre,tipo,ejemplares in animales:
        if nombre.lower() == especie.lower():
            if ejemplares == 0:
                return "Extinto"
            elif ejemplares <= 500:
                return "En peligro critico"
            elif ejemplares <= 2000:
                return "En peligro"
            else:
                return "Amenazado"
    raise ValueError(f"La especia '{especie}' no estaba en la lista")

# --- PRUEBAS ---
print(comprobar_estado("oso pardo"))        # En peligro crítico (prueba el 500 exacto y minúsculas)
print(comprobar_estado("LINCE IBÉRICO"))    # En peligro (prueba mayúsculas)
print(comprobar_estado("Lobo ibérico"))     # Amenazado

# Prueba de la excepción
try:
    print(comprobar_estado("Tigre"))
except ValueError as e:
    print("Error capturado:", e)