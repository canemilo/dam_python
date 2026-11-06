from anexo import series
#3. Muestra los títulos de las series que tengan una nota igual o superior a 9 y que
#además tengan 3 o más géneros.
listas = [
    s["titulo"]
    for s in series if "nota" >= 9 and "generos"  
]

print(listas)