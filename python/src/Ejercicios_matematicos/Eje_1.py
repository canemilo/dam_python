try:
    # Pedir el número entero al usuario
    numero = int(input("Introduce un número entero mayor o igual a 1: "))

    # Validar si es menor que 1
    if numero < 1:
        print(" Error: El número debe ser mayor o igual a 1.")
    else:
        # Calcular el sumatorio usando un bucle
        sumatorio = 0
        for i in range(1, numero + 1):
            sumatorio = sumatorio + i

        print(f" El sumatorio desde 1 hasta {numero} es: {sumatorio}")

except ValueError:
    print(" Error: Debes introducir un número entero válido.")