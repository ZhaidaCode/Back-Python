# Tabla de multiplicaar de un numero
numero = 0
for  numero in range (1,5):
    print("Tabla de multiplicar del", numero)
    for i in range (1,11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
