from anexo import series

lista = [g for s in series for g in s["generos"]]

print(lista)