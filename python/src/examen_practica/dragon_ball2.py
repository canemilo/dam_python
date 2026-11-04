from datos import personajes

def ej1():
    nuevo_personaje = { "nombre":"Freezer",
                       "raza":"namek",
                       "nivel_pelea":77000000,
                       "tecnicas":["Galick ho","Destruccion"],
                       "atributos":{"fuerza":77,"defensa":77,"velocidad":88}}


    personajes.append(nuevo_personaje)
    
    for personaje in personajes:
        print(personaje)
        
        
def ej2():
    for personaje in personajes:
        media = (personaje["atributos"]["fuerza"] + personaje["atributos"]["defensa"] + personaje["atributos"]["velocidad"] / 3)
        if media > 80:
            print(personaje)
        
def ej3():
    suma = 0
    for personaje in personajes:
        suma += (personaje["atributos"]["velocidad"])
        
    media = suma / len(personajes)
    
    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media:
            print(personaje)
            
def ej4():
    for personaje in personajes:
        for tecnica in personaje["tecnicas"]:
            if tecnica == "Big Bang Attack":
                if personaje["atributos"]["fuerza"] + 10 <= 100:
                    personaje["atributos"]["fuerza"] += 10
                else:
                    personaje["atributos"]["fuerza"] = 100
                    
        print(personaje["nombre"],personaje["atributos"]["fuerza"])
        
        
def ej5():
    elegido = " "
    for personaje in personajes:
        if personaje["nombre"] == "Vegeta":
            elegido = personaje["atributos"]["fuerza"]
            break
        
    for personaje in personajes:
        if personaje["atributos"]["defensa"] < elegido and personaje["nombre"] != "Vegeta":
            print(personaje["nombre"],personaje["atributos"]["defensa"])
            
            
def ej6():
    for personaje in personajes:
        if personaje["raza"] == "Saiyan":
            personajes.remove(personaje)
            
    print(personajes)