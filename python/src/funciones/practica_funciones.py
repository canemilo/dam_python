import math  # <-- Añade esta línea arriba del todo


def funcion1():
    print("Esta es la función 1")


"""

ejercicio 2 Convertir Temperatura 

"""
def convertirTemperatura(grados, unidad_origen, unidad_destino):
    # 1. Pasamos la temperatura inicial a Celsius
    if unidad_origen == "C":
        celsius = grados
    elif unidad_origen == "F":
        celsius = (grados - 32) * 5 / 9
    elif unidad_origen == "K":
        celsius = grados - 273.15

    # 2. Pasamos de Celsius a la unidad que nos piden
    if unidad_destino == "C":
        resultado = celsius
    elif unidad_destino == "F":
        resultado = (celsius * 9 / 5) + 32
    elif unidad_destino == "K":
        resultado = celsius + 273.15

# 3 Redondeamos al final para 2 decimales
    return round(resultado, 2)



print(convertirTemperatura(10, "F", "C")) 


"""""
Ejercicio 3 calcularValorBruto

"""

def calcularValorBruto(precio,cadena):

    if cadena == "GENERAL":
        porcentaje = 0.21 
    elif cadena == "REDUCIDO":
        porcentaje = 0.10
    elif cadena == "SUPERREDUCIDO":
        porcentaje = 0.04
    else:
        return "Tipo de IVA no valido"

    #2 Calcular cuanto dinero es el iva y lo sumamos al precio
    iva = precio * porcentaje
    total = precio + iva

    #3 Redondear hacia arriba con 2 decimales
    resultado = math.ceil(total*100)/100

    return resultado



## RESULTADO ##
print("RESULTADOS CALCULAR VALOR BRUTO")
print(calcularValorBruto(10,"GENERAL"))
print(calcularValorBruto(10,"REDUCIDO"))
print(calcularValorBruto(10,"SUPERREDUCIDO"))
print(calcularValorBruto(10.555,"GENERAL"))


"""
Ejercicio 4 Crea una función llamada convertirLongitud 
que reciba un número con decimales y dos cadenas de caracteres. 
Las cadenas de caracteres posibles serán "M", "YD" y "FT", 
que representan unidades de medida (Metros, Yardas y Pies). 
La función devolverá, como número con decimales, 
el resultado de convertir de la primera unidad que reciba la función a la segunda. 
Por ejemplo, convertirLongitud(10, "M", "YD") 
devolvería el resultado de pasar 10 metros a yardas. 
Devuelve el resultado con tres decimales, redondeando al valor más cercano.

"""

def convertirLongitud(numero,cadena1,cadena2):
  # Normalizamos las cadenas a mayúsculas para evitar errores
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    
    # Paso 1: Convertir la unidad inicial (cadena1) a metros
    if cadena1 == "M":
        metros = numero
    elif cadena1 == "YD":
        metros = numero / 1.09361
    elif cadena1 == "FT":
        metros = numero / 3.28084
    else:
        return "Unidad de origen no válida"

    # Paso 2: Convertir de metros a la unidad destino (cadena2)
    if cadena2 == "M":
        resultado = metros
    elif cadena2 == "YD":
        resultado = metros * 1.09361
    elif cadena2 == "FT":
        resultado = metros * 3.28084
    else:
        return "Unidad de destino no válida"

    return round(resultado, 4)
print("RESULTADOS Convertir Longitud")
# USO
print(convertirLongitud(10, "M", "YD"))   
print(convertirLongitud(10, "M", "FT"))   
print(convertirLongitud(30, "FT", "YD"))  


"""
Crea una función llamada aplicarDescuentoFidelidad,
que reciba un número con decimales (el importe de una compra)
y una cadena de caracteres (que representará la categoría del cliente).
Las cadenas de caracteres posibles serán "PREMIUM", "ESTANDAR" y "NUEVO". 
La función devolverá el resultado de restar al importe el porcentaje de descuento 
correspondiente (PREMIUM tiene un 15% de descuento, ESTANDAR un 5% y NUEVO un 0%). 
Por ejemplo, aplicarDescuentoFidelidad(50, "PREMIUM") 
devolvería el resultado de restar a los 50€ el 15%, lo que daría 42,50€.
Devuelve el resultado con dos decimales, redondeando siempre hacia abajo 
(para que el redondeo beneficie al cliente).
"""



def aplicarDescuentoFidelidad(importe_decimales, cadena_usuario):
    categoria = cadena_usuario.upper()

    if categoria == "PREMIUM":
        resultado = importe_decimales * 0.85
    elif categoria == "ESTANDAR":
        resultado = importe_decimales * 0.95
    elif categoria == "NUEVO":
        resultado = importe_decimales
    else:
        raise ValueError(f"Categoría no válida: '{cadena_usuario}'")

    # Redondeo 
    return math.floor(resultado * 100) / 100


# --- PRUEBAS ---
print(aplicarDescuentoFidelidad(50, "PREMIUM"))     
print(aplicarDescuentoFidelidad(19.99, "estandar")) 
print(aplicarDescuentoFidelidad(10.999, "NUEVO"))   