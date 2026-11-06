from anexo import series

#5. Muestra una lista con los comentarios que tengan más de 40 caracteres.
lista = [r["comentario"] for s in series for r in s["reseñas"] if len(r["comentario"]) > 40]

print(lista)