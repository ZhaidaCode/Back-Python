# Ejemplo 1 - ValueError
print("------Ejemplo 1 ------")
try:
    edad = int("veinte")
    print("Edad:", edad)
except ValueError:
    print("Error: Debes ingresar un número")

print("\n -----Ejemplo 2 ------")
try: 
    resultado = 10 / 2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

print("\n -----Ejemplo 3 ------")
perfil = {"nombre": "Zhaida", "meta": "Yape"}
try:
    print(perfil["salario"])
except KeyError:
    print("Error: La clave 'salario' no existe en el perfil")

print("\n -----Ejemplo 4 ------")
try:
    numero = int("100")
except ValueError:
    print("Error: No se pudo convertir a número")   
finally:
    print("Proceso terminado")