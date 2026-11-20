"""
Dada la lista de servidores dispuesta más abajo, crea una función llamada evaluar_servidor
que reciba el nombre de un servidor y 
devuelva su estado según el porcentaje de uso de CPU:
Si el uso de CPU es 0, devuelve "Apagado".
Si es mayor que 0 y menor o igual que 50, devuelve "Óptimo".
Si es mayor que 50 y menor o igual que 85, devuelve "Carga alta".
Si es mayor que 85, devuelve "Sobrecargado".
Si el servidor no existe en la lista, lanza una excepción con raise ValueError.
Debe dar igual si el nombre se pasa en mayúsculas o minúsculas.

"""


servidores = [
    ["Auth-Server", "Madrid", 35],
    ["DB-Principal", "Frankfurt", 92],
    ["Backup-01", "Irlanda", 0],
    ["API-Gateway", "París", 70]
]

# convertir lista en diccionario
servidores_dic = {nombre.lower() : {"ciudad":ciudad,"cpu":cpu} for nombre,ciudad,cpu in servidores}


def evaluar_servidor(nombre):
    clave = nombre.lower()
    
    # 1. comprobar
    if clave not in servidores_dic:
        raise ValueError(f"El servidor '{nombre}' no esta en la lista")
    
    # 2. acceso directo
    cpu = servidores_dic[clave]["cpu"]
    
    if cpu == 0:
        return "Apagado"
    elif cpu <= 50:
        return "Optimo"
    elif cpu <= 85:
        return "Carga alta"
    else:
        return "Sobrecargado"

try:
    print(evaluar_servidor("Auth-Server"))
except ValueError as e1:
    print("Error capturado:",e1)
    
try:
    print(evaluar_servidor("dbPrincipal"))
except ValueError as e2:
    print("Error capturado:",e2)
    
try:
    print(evaluar_servidor("Api"))
except ValueError as e:
    print("Error capturado:", e)
