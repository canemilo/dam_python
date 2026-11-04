from datos import series

def eje1():
    listas = [
        serie["titulo"]
        for serie in series
            if "Animación" in serie["generos"]
    ]

    print(listas)
    
    
def eje2():
    listas = [
        serie["titulo"]
        for serie in series
            if "Fantasía" in serie["generos"] or "Misterio" in serie["generos"]]

    print(listas)
    

def eje3():
    listas = [
        serie["titulo"]
        for serie in series
            if serie["nota"] >= 9 and len(serie["generos"]) >= 3
    ]    
    print(listas)

def eje4():
    tuplas = [
        (serie["titulo"],resena["nota"])
        for serie in series
            for resena in serie["reseñas"] if resena["usuario"] == "Elena"
        
    ]
    print(tuplas)
    
def eje5():
    listas = [
       resena["comentario"]
       for serie in series
        for resena in serie["reseñas"]
            if len(resena["comentario"]) > 40
        
        
    ]
    print(listas)
    
def eje6():
   listas = [f"La serie {s['titulo']} tiene {len(s['reseñas'])} reseñas" for s in series]
   print(listas)
   
def eje7():
    tuplas = [
        (serie["titulo"], resena["comentario"])
        for serie in series for resena in serie["reseñas"] if resena["nota"] == 10
    ]
    
    print(tuplas)
    
def eje8():
    tuplas = [(serie["titulo"],"Obra Maestra")if serie["nota"] >= 9 else "Gran serie"
              for serie in series
              
              
              
              ]
    print(tuplas)
    
def eje9():
    lista = [gen for s in series for gen in s["generos"]]

    print(lista)