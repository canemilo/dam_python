from anexo import series


lista = [
    (serie["titulo"], "Obra maestra" if serie["nota"] >= 9 else "Gran serie") 
    for serie in series
]

print(lista)