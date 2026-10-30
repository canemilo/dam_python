from anexo import series
listas = [
    s["titulo"]
    for s in series
    if "Animación" in s["generos"]
]

print(listas)