# Sistema de seguimiento de habilidades

def agregar_habilidad(lista, habilidad):
    lista.append(habilidad)
    print("Habilidad agregada:", habilidad)

def mostrar_progreso(nombre, habilidades, meta):
    print("======", nombre, "======")
    print("Meta:", meta)
    print("Habilidades adquiridas:")
    for h in habilidades:
        print("  ✓", h)
    print("Total:", len(habilidades), "de", len(meta))
          
    if len(habilidades) >= 15:
        print("Estado: Lista para aplicar a empresas")
    elif len(habilidades) >= 10:
        print("Estado: En camino a la meta")
    elif len(habilidades) >= 2:
        print("Estado: empezando el camino tech")
    else:
        print("Estado: arrancando, no pares!")

mis_habilidades = []

agregar_habilidad(mis_habilidades, "Python")
agregar_habilidad(mis_habilidades, "Git")
agregar_habilidad(mis_habilidades, "Github")
agregar_habilidad(mis_habilidades, "Listas")
agregar_habilidad(mis_habilidades, "Diccionarios")
agregar_habilidad(mis_habilidades, "Funciones")
agregar_habilidad(mis_habilidades, "Bucles")
agregar_habilidad(mis_habilidades, "Condicionales")

print("==========================")

mostrar_progreso("Zhaida", mis_habilidades, "Trabajar en yape o mercado libre")