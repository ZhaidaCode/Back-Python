# Mi lista de habilidades
habilidades = ["Python", "Git", "GitHub", "VS Code", "Condicionales", "Bucles", "Funciones"]

print("===MIS HABILIDADES ACTUALES===")
for habilidad in habilidades:
    print("✓", habilidad)

print("Total de habilidades:", len(habilidades))

print("=================================")

#Agregar nuevas habilidades 
habilidades.append("Listas")
print("Nueva habilidad agregada!")
print("Total ahora:", len(habilidades))

print("=================================")

#Acceder por indice
print("Mi primera habilidad aprendida:", habilidades[0])
print("M habilidad mas reciente:", habilidades[-1])