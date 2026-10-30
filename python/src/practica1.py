def main():
    # 5.2. Crea una lista con los siguientes elementos
    lista_1 = ["Manzana", "Pera", "Melocotón"]
    
    # 5.3. Crea otra lista con los siguientes elementos
    lista_2 = ["Kiwi", "Sandía", "Melón"]
    
    # 5.4. Añade la segunda lista a la primera
    lista_1.extend(lista_2)
    
    # 5.5. Muestra el último elemento de la lista
    print("Último elemento de la lista:", lista_1[-1])
    
    # 5.6. Crea una tupla con los números 3, 5 y 7
    mi_tupla = (3, 5, 7)
    
    # 5.7. Muestra el primer elemento de la tupla
    print("Primer elemento de la tupla:", mi_tupla[0])
    
    # 5.8. Crea un rango con parámetros dados por el usuario
    print("\n--- Configuración del rango ---")
    inicio = int(input("Introduce el valor de inicio: "))
    fin = int(input("Introduce el valor de fin: "))
    salto = int(input("Introduce el valor de salto: "))
    
    mi_rango = range(inicio, fin, salto)
    
    # 5.9. Muestra el rango
    print("\nObjeto rango:", mi_rango)
    print("Valores dentro del rango:", list(mi_rango))

# 5.1. Crea la estructura de programa principal
if __name__ == "__main__":
    main()
# pip freeze > dependencias.txt
# # pip install jupyterlab
## pip freeze > dependencias.txt
# entorno-practica\Scripts\activate
# jupyter notebook