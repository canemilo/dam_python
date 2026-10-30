edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario < 0 or edadUsuario > 120:
    print("Es un vampiro")
elif edadUsuario >=18 :
    print("Es mayor de edad")
else:
    print("Error")


edadUsuario2 = int(input("Ingrese su edad: "))


match edadUsuario2:
    case x if x < 0 or x > 120:
        print("Es un vampiro")
    case x if x > 18:
        print("Es mayor de edad")
    case _:
        print("Error")