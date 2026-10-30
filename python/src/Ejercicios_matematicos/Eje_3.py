

base = int(input("Escribe numero base: "))
potencia = int(input("Escribe numero potencia: "))

if(base < 1 or potencia < 0 ):
    print("error ")
else:
    resultado = 1;                      ########################################
    for i in range(1, potencia  + 1): ## -->  (base**potencia) hace lo mismo <-- ##
        resultado = resultado * base    ########################################
    print("RESULTADO : " , resultado)