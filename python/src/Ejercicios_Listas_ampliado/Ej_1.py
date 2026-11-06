from anexo import series

#1. Muestra una lista con los títulos de las series que sean de Animación.
listas = [
    s["titulo"]
    for s in series
    if "Animación" in s["generos"]
]

print(listas)