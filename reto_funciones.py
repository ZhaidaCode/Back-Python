# Mini calculadora con funciones
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

#Probando la calculadora
print("Suma:", suma(10, 5))
print("Resta:", resta(10, 5))
print("Multiplicación:", multiplicacion(10, 5))
print("División:", division(10, 5))
print("División por cero:", division(10, 0))