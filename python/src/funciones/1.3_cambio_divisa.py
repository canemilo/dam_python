"""
Vamos a crear una función que permita convertir entre diferentes tipos de
divisas.

Crea una función llamada cambiar_divisa que reciba como parámetros una
cantidad de dinero (que puede tener decimales), un string que represente la
divisa en la que está, y otro string que represente la divisa en la que
queramos convertir el dinero. La función devolverá el equivalente en la
segunda divisa del dinero especificado en la primera divisa. Así, la función
cambiar_divisa(10, “euro”, “dolar”) devolverá 10’90 dólares.
Las divisas se escribirán sin tilde y será indiferente que estén en mayúsculas
o minúsculas.
La función permitirá cambiar entre euros, dólares y yenes, y devolverá el
resultado con 3 decimales. A continuación tienes los tipos de cambio entre
estas divisas:


"""

tasas = {
    ("euro", "dolar"): 1.09,
    ("euro", "yen"): 163.38,
    ("dolar", "euro"): 0.92,
    ("dolar", "yen"): 149.67,
    ("yen", "euro"): 0.0061,
    ("yen", "dolar"): 0.0067
}

def cambiar_divisa(cantidad,origen,destino):
    origen = origen.lower()
    destino = destino.lower()
    
    # 1. Si pide cambiar a la misma divisa (ej. "euro" a "euro")
    if origen == destino:
          if origen in ("euro","dolar","yen"):
              return round(cantidad,3)
          raise ValueError(f"Divisa no valida : '{origen}'")
      
    # 2. comprobar si la pareja origen-destino existe
    if (origen,destino) not in tasas:
        raise ValueError(f"No se puede convertir de '{origen}' a '{destino}'")
    
    # 3. Buscar el multiplicador exacto
    resultado = cantidad * tasas[(origen, destino)]
    return round(resultado,3)

### PRUEBAS

print(cambiar_divisa(100,"euro","dolar"))
print(cambiar_divisa(50,"yen","dolar"))
print(cambiar_divisa(200,"dolar","euro"))

try:
    print(cambiar_divisa(100,"peso","euro"))
except ValueError as e:
    print("Error capturado: ",e)
    
    