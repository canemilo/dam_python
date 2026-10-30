from anexo import series

lista = [n["usuario"] for s in series for n in s["reseñas"] if "Drama" in s["generos"]]

print(lista)