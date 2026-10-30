from anexo import series

listas = [
    s["titulo"]
    for s in series if "nota" >= 9 and "generos"  
]

print(listas)