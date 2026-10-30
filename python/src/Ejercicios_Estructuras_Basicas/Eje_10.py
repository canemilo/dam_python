# 1
inicio = int(input("Ingrese el primer número (inicio): "))
fin = int(input("Ingrese el segundo número (fin): "))

if inicio > fin:
    print("Error: El primer número no puede ser mayor que el segundo.")
else:
    print(f"Números primos entre {inicio} y {fin}:")

    # 3. Recorrer
    for num in range(inicio, fin + 1):
        if num > 1:
            es_primo = True


            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break


            if es_primo:
                print(num, end=" ")

