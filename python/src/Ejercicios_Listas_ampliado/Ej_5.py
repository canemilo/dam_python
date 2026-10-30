from anexo import series


lista = [r["comentario"] for s in series for r in s["reseñas"] if len(r["comentario"]) > 40]

print(lista)