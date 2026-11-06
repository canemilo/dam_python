from anexo import series
#4. Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el
#usuario Elena.
lista = [(s["titulo"], r["nota"]) for s in series for r in s["reseñas"] 
         if r["usuario"] == "Elena" ]
print(lista)