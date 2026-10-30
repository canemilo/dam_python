
numeroUsuario = float(input("Ingrese precio producto: "))
ivaUsuario = input("Ingrese Tipo de IVA : ( GENERAL;REDUCIDO;SUPERREDUCIDO )").lower()


match ivaUsuario.lower():
    case "GENERAL":
        porcentaIVA = 0.0 * numeroUsuario
        print(porcentaIVA)
    case "REDUCIDO":
        porcentaIVA = 0.0 * numeroUsuario
        print(porcentaIVA)
    case "SUPERREDUCIDO":
        porcentaIVA = 0.0 * numeroUsuario
        print(porcentaIVA)

    case _:
        print("error")

