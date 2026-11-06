
# 2.2 ejercicio 1
def sumatorio(n : int) -> int:
    sumatorio = 0
    for i in range(1, n + 1):
        sumatorio += i
    return sumatorio
print(sumatorio(2))

# ejercicio 2

def pedirNumero(n : int) -> int:
    resultado = 1
    for i in range(1,n+1):
        resultado *=i
    return resultado

print(pedirNumero(3))


# ejercicio 3
def pedirDosNumerosEnteros(base:int,potencia:int)->int:
    resultado = 0
    resultado = base ** potencia
    return resultado

print(pedirDosNumerosEnteros(2, 3))
