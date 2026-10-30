numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un numero entero: "))

## VERSION F O R    ###

for i in range(numero1,numero2):
    if i % 2 == 0:
        print(i)






## VERSION WHILE ##

print("Versión con WHILE:")
actual = numero1
while actual <= numero2:
    if actual % 2 == 0:
        print(actual,end=" ")
    actual += 1
print()