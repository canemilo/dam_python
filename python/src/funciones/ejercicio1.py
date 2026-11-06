def comprobarLetraDNI(n: String) -> bool:  
    letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    soloNumeros = int(n[:-1])
    resto = soloNumeros % 23
    
    letraCorrecta = letras[resto]
    
    if n[-1].upper() == letraCorrecta:  
        return True
    else:
        return False

print(comprobarLetraDNI("25734945S"))
print(comprobarLetraDNI("24843238H"))
print(comprobarLetraDNI("24843238X"))




## CONVERTIR TEMPERATURA 


def convertirTemperatura(n:float,s1:String,s2:String)-> float:
    resultado = 0.0
    opcionesLetras = ["C","K","F"]

    return resultado