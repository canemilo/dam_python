from datos import personajes

def ejercicio1():
    lista = [p["nombre"] for p in personajes if "Cuerpo de Exploración" in p["afiliacion"]]
    print(lista)

def ejercicio2():
   listas = [
    s["nombre"]
    for s in personajes
    if "Cuerpo de Exploración" in s["afiliacion"] or "Supervivencia" in s["habilidades"] or "Sigilo" in s["habilidades"]]
   print(listas)


def ejercicio5():
    tuplas = [(personaje["nombre"], personaje["estatura_m"])
              for personaje in personajes 
              if personaje["estatura_m"] >= 1.70]
    print(tuplas)

def ejercicio6():
    lista = [g for s in personajes for g in s["habilidades"]]
    print(lista)

