# Mi perfil developer como diccionario
perfil = {
    "nombre": "Zhaida",
    "pais": "Peru",
    "meta": "Trabajar en mercado libre o yape",
    "meses para meta": 12,
    "estudiando": "Python"
}

print("=====Mi perfil developer=====")
for clave, valor in perfil.items():
    print(clave + ":", valor)

print("========================================")

#Agregar habilidades
perfil["habilidades"] = ["Python", "Git", "Github", "Listas", "Diccionarios"]

print("Habilidades:", perfil["habilidades"])
print("Total habilidades:", len(perfil["habilidades"]))
