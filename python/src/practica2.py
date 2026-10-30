
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


#2. Pedir al usuario dos valores por pantalla: el precio de un producto
# (float) y el tipo de IVA (General, Reducido, Superreducido).
# Calcular el precio final del producto fruto de sumarle el IVA en función de su tipo. Realizar una versión con IF y otra con MATCH.



precio_base = float(input("Ingrese el precio del producto: "))

print("Tipos de IVA disponibles: General, Reducido, Superreducido")
tipo_iva = input("Ingrese el tipo de IVA: ").strip().capitalize()


porcentaje_iva = 0.0

# ==========================================
# VERSIÓN 1: Usando IF - ELIF - ELSE
# ==========================================
if tipo_iva == "General":
    porcentaje_iva = 0.21
elif tipo_iva == "Reducido":
    porcentaje_iva = 0.10
elif tipo_iva == "Superreducido":
    porcentaje_iva = 0.04
else:
    print("Tipo de IVA no válido. Se aplicará un 0% por defecto.")

# Calcular el precio final
precio_final = precio_base + (precio_base * porcentaje_iva)
print(f"[IF] El precio final con IVA ({tipo_iva}) es: {precio_final:.2f} €")


# ==========================================
# VERSIÓN 2: Usando MATCH - CASE (Python 3.10+)
# ==========================================
match tipo_iva:
    case "General":
        porcentaje_iva = 0.21
    case "Reducido":
        porcentaje_iva = 0.10
    case "Superreducido":
        porcentaje_iva = 0.04
    case _:
        porcentaje_iva = 0.0
        print("Tipo de IVA no válido en match. Se aplicará un 0%.")

precio_final_match = precio_base + (precio_base * porcentaje_iva)
print(f"[MATCH] El precio final con IVA ({tipo_iva}) es: {precio_final_match:.2f} €")
