password_correcta = "12345"

while True:
    password_introducida = input("Introduce la contraseña: ")

    if password_introducida == password_correcta:
        print("¡Bienvenido! Has accedido correctamente.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.\n")