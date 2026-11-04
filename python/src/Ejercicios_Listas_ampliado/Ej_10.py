from anexo import series
#10. Muestra una lista con todos los nombres de los usuarios que hayan opinado en
#alguna serie de Drama. No importa si hay nombres repetidos.
lista = [n["usuario"] for s in series for n in s["reseñas"] if "Drama" in s["generos"]]

print(lista)