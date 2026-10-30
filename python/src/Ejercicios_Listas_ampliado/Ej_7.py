from anexo import series

lista = [ (s["titulo"], r["comentario"]) 
         for s in series 
            for r in s["reseñas"] 
                if r["nota"] == 10
]

print(lista)