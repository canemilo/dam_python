
# ejercicio 1
# Pedir al usuario una nota numérica entera mediante un input y
# diga si la calificación es Suspenso, Aprobado, Notable, Sobresaliente,
# o No válida (en caso de que la entrada sea diferente a la esperada). Realizar una versión con IF y otra con MATCH.

numero = int(input("Ingrese nota del 0 al 10: "))

if numero >= 0 and numero < 5:
    print("Suspenso")
elif numero >= 5 and numero < 7:
    print("Aprobado")
elif numero >= 7 and numero < 9:
    print("Notable")
elif numero >= 9 and numero <= 10:
    print("Sobresaliente")
else:
    print("Erro")
