# Funciones que buscan en una lista
def buscar_empresa(empresas, nombre):
    for empresa in empresas:
        if empresa["nombre"] == nombre:
            return empresa
    return None

# Mi lista de empresas
empresas = [
    {"nombre": "Mercado libre", "pais":"Argentina", "area": "Backend Pyhton"},
    {"nombre": "Yape", "pais": "Peru", "area": "Backend Python"},
    {"nombre": "Google", "pais": "Estados Unidos", "area": "Backend Python"},
    {"nombre": "Facebook", "pais": "Estados Unidos", "area": "Backend Python"},
    {"nombre": "Amazon", "pais": "Estados Unidos", "area": "Backend Python"}
    ]

resultado = buscar_empresa(empresas, "Google")

if resultado:
    print("Empresa encontrada:")
    print("Nombre:", resultado["nombre"])
    print("Pais:", resultado["pais"])
    print("Area:", resultado["area"])
else:
    print("Empresa no encontrada")