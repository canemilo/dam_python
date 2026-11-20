# funciones

print("hola mundo")

print('python','es','genial',sep="-")

print("esto se imprime",end =' ')
print("en una linea")
print()
print("sumar un numero y una cadena de texto")
print(2 + int("100"))

print()
print("variables")

nombreVariable = 'daniel'
print(nombreVariable)
print(f'Cambio de nombreVariable de string a number')
nombreVariable = 38
print(nombreVariable)

print('tu nombre es ', nombreVariable)
#print(input('Escribe tu nombre : '))
MI_CONSTANTE = 3.14


print('Mi contstante :',{MI_CONSTANTE})
# al ponerle :bool documentamos que esa variable es boolean, pero no sirve para tiparla
verdadero_falso :bool = True
print(verdadero_falso)
verdadero_falso = 'Daniel'
print(verdadero_falso)
print()
print(f'INPUNT')

nombre = input('Hola como te llamas :')
print(f"Hola {nombre} , encantado ")

age = input("Cuantos años tienes?\n")
print(f"Dentro de 20 años tendras {int(age) + 20}")
print()
print(f'obtener multiples valores')

pais,ciudad = input("En que pais y ciudad vives\n").split()

print(f"*****Vives en {pais},{ciudad}*********")