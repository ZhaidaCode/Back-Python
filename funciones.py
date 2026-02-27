#Función simple
def mostrar_bienvenida():
    print("Bienvenida al mundo backend!")

mostrar_bienvenida()

print("-----------------------------------------")

# Función con parametros
def presentar_developer(nombre, pais, meta):
    print("Nombre:", nombre)
    print("País:", pais)
    print("Meta:", meta)
presentar_developer("Zhaida", "Peru", "Trabajar en yape o mercado libre")

print("-----------------------------------------")

#Función que devuelve un valor
def calcular_progreso(meses_estudiados, meses_totales):
    porcentaje = meses_estudiados / meses_totales * 100
    return porcentaje

mi_progreso = calcular_progreso(1, 12)
print("Mi progreso es del:", mi_progreso, "%")