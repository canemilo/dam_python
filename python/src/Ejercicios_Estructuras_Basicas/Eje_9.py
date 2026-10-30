numUsuario = int(input("Ingrese un número: "))

if numUsuario > 1:
    es_primo = True
    # Revisamos los divisores desde 2 hasta numUsuario - 1 ( el ultimo numero no entra en la division )
    for i in range(2, numUsuario):
        if numUsuario % i == 0:
            es_primo = False
            break  # Si encuentra un divisor, ya no es primo y sale del bucle

    if es_primo:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
else:
    print("NO ES PRIMO")