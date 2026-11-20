def sumatorio(n):
    if n < 0:
        raise ValueError("Para el sumatorio el número debe ser mayor o igual a 0.")
    
    total = 0
    for i in range(0, n + 1):
        total += i
    return total


def factorial(n):
    if n < 1:
        raise ValueError("Para el factorial el número debe ser mayor o igual a 1.")
    
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def aplicar_funcion(valor, operacion):
    operacion = operacion.lower()
    
    try:
        if operacion == "sumatorio":
            return sumatorio(valor)
        elif operacion == "factorial":
            return factorial(valor)
        else:
            print(f"Error: la operación '{operacion}' no es válida.")
    except ValueError as e:
        print(f"Error: {e}")


# --- PRUEBAS ---
print(aplicar_funcion(3, "factorial"))   # 6 (1 * 2 * 3)
print(aplicar_funcion(5, "sumatorio"))   # 15 (0 + 1 + 2 + 3 + 4 + 5)
print(aplicar_funcion(0, "sumatorio"))   # 0

# Casos de error
aplicar_funcion(-3, "factorial")         # Error: Para el factorial el número debe ser mayor o igual a 1.
aplicar_funcion(-1, "sumatorio")         # Error: Para el sumatorio el número debe ser mayor o igual a 0.
aplicar_funcion(4, "potencia")           # Error: la operación 'potencia' no es válida.