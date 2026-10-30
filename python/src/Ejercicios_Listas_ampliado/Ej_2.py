from anexo import series

listas = [
    s["titulo"]
    for s in series
    if "Fantasía" in s["generos"] or "Misterio" in s["generos"]
]

print(listas)