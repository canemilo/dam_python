from anexo import series


listas = [f"La serie {s['titulo']} tiene {len(s['reseñas'])} reseñas" for s in series]

print(listas)