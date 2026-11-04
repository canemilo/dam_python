from datos import personajes


def ejercicio1():
    nuevo_personaje = {
        "nombre" : "Krilin",
        "raza" : "Humano",
        "nivel_pelea" : 12000000,
        "tecnicas" : ["Morir", "Comer"],
        "atributos" : {"fuerza" : 30, "defensa" : 45, "velocidad" : 66}
    }
    personajes.append(nuevo_personaje)
    
    for p in personajes:
            print(p)
            
def ejercicio2():
    for personaje in personajes:
        media = (personaje["atributos"]["fuerza"] + personaje["atributos"]["defensa"] + personaje["atributos"]["velocidad"] / 3 )
        
        if media > 80:
            print(personaje)
            
            
def ejercicio3():
    suma = 0
    
    for personaje in personajes:
        suma += (personaje["atributos"]["velocidad"] )
        
    # fuera del bucle
    media = suma / len(personajes)
    
    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media:
            print(personaje)
            
            
def ejercicio4():
    sumaPuntos = 10
    
    for personaje in personajes:
        for tecnica in personaje["tecnicas"]:
            if tecnica == "Big Bang Attack":
                if personaje["atributos"]["fuerza"] + 10 <= 100:
                        personaje["atributos"]["fuerza"] += 10
                else:
                    personaje["atributos"]["fuerza"] = 100
    
        print(personaje["nombre"],personaje["atributos"]["fuerza"])
            
            
def ejercicio5():
    elegido = ""
    for personaje in personajes:
        if personaje["nombre"] == "Vegeta":
            elegido = personaje["atributos"]["fuerza"]
            break
        
    for personaje in personajes:
        if personaje["atributos"]["defensa"] < elegido and personaje["nombre"] != "Vegeta":
            print(personaje["nombre"], personaje["atributos"]["defensa"])
            
            
def ejercicio6():
    for personaje in personajes:
        if personaje["raza"] == "Saiyan":
            personajes.remove(personaje)
            
        print(personajes)
        