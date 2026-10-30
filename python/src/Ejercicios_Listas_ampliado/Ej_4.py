from anexo import series

lista = [(s["titulo"], r["nota"]) for s in series for r in s["reseñas"] 
         if r["usuario"] == "Elena" ]
print(lista)