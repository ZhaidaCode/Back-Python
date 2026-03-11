# Lista de empresas donde quiero trabajar
empresas = [
    {"nombre": "Mercado Libre", "pais": "Argentina", "area": "Backend Python"},
    {"nombre": "Yape", "pais": "Peru", "area": "Backend Python"},
    {"nombre": "Google", "pais": "Estados Unidos", "area": "Backend Python"},
    {"nombre": "Facebook", "pais": "Estados Unidos", "area": "Backend Python"},
    {"nombre": "Amazon", "pais": "Estados Unidos", "area": "Backend Python"}
]

print("======Empresas objetivo======")
for empresa in empresas:
    print("Nombre:", empresa["nombre"])
    print("Pais:", empresa["pais"])
    print("Area:", empresa["area"])
    print("-----------------------------")
print("Total empresas objetivo:", len(empresas))