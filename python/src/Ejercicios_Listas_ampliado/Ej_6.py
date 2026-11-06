from anexo import series

#6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
#todas las series.
listas = [f"La serie {s['titulo']} tiene {len(s['reseñas'])} reseñas" for s in series]

print(listas)