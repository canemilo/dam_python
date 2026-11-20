class Jarra:
    def __init__(self, capacidad: int, contenido: int = 0):
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        if contenido < 0:
            raise ValueError("El contenido no puede ser menor que cero.")
        
        self.capacidad = capacidad
        # Si el contenido supera la capacidad, se ajusta al máximo permitido
        self.contenido = min(contenido, capacidad)

    def llenar(self):

        self.contenido = self.capacidad

    def vaciar(self):

        self.contenido = 0

    def servir(self, cantidad: int):

        if cantidad < 0:
            raise ValueError("La cantidad a servir no puede ser negativa.")
        if cantidad > self.contenido:
            raise ValueError("No hay suficiente contenido en la jarra.")
        
        self.contenido -= cantidad

    def llenar_desde(self, otra_jarra: "Jarra"):

        espacio_disponible = self.capacidad - self.contenido
        cantidad_a_transferir = min(espacio_disponible, otra_jarra.contenido)
        
        otra_jarra.servir(cantidad_a_transferir)
        self.contenido += cantidad_a_transferir

    def __str__(self):
        return f"Jarra({self.contenido}/{self.capacidad})"


# Ejemplo de uso
if __name__ == "__main__":
    jarra_a = Jarra(5, 8)  # Se ajusta automáticamente a 5/5
    jarra_b = Jarra(7)     # Empieza en 0/7

    print(f"Inicio -> A: {jarra_a}, B: {jarra_b}")

    jarra_b.llenar_desde(jarra_a)
    print(f"Tras pasar de A a B -> A: {jarra_a}, B: {jarra_b}")

    jarra_b.servir(2)
    print(f"Tras servir 2 de B -> B: {jarra_b}")

    jarra_a.llenar()
    jarra_b.llenar_desde(jarra_a)
    print(f"Tras llenar A y pasar a B -> A: {jarra_a}, B: {jarra_b}")