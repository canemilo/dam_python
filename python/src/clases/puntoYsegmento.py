class Punto:
    def __init__(self,cordenadaX:int = 0,cordenadaY:int = 0):

         if not (-100 <= cordenadaX <= 100) or not (-100 <= cordenadaY <= 100):
            raise ValueError("Las coordenadas deben estar comprendidas entre -100 y 100.")
    
         self.cordenadaX = cordenadaX
         self.cordenadaY = cordenadaY


    def __str__(self):
        return f"Punto ({self.cordenadaX} , {self.cordenadaY})"

    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return False
        return self.coordenadaX == otro.coordenadaX and self.coordenadaY == otro.coordenadaY



class Segmento:
    def __init__(self,puntoA:Punto = (0,0),puntoB:Punto = (1,1)):

        self.puntoA = puntoA
        self.puntoB = puntoB

    def __str__(self):
        return f"Segmento[{self.puntoA},{self.puntoB}]"

    def longitud(self):
             

