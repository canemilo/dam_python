from anexo import series
#8. Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las
#notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso
#contrario.
lista = [
    (serie["titulo"], "Obra maestra" if serie["nota"] >= 9 else "Gran serie") 
    for serie in series
]

print(lista)