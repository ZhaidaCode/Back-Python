def dividir_seguro(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"

def convertir_numero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: No se pudo convertir a número"

def buscar_dato(diccionario, clave):
    try:
        return diccionario[clave]
    except KeyError:
        return f"Error: La clave '{clave}' no existe en el diccionario"
    
#Probando todo
print("-------Calculadora segura-------")
print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

print("\n-------Conversión segura-------")
print(convertir_numero("100"))
print(convertir_numero("cien")) 

print("\n-------Búsqueda segura-------")
diccionario = {"nombre": "Zhaida", "meta": "Yape"}
print(buscar_dato(diccionario, "nombre"))
print(buscar_dato(diccionario, "salario"))       
