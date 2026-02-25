# Bucle for con range

print("======Contando del 1 al 5 ======")
for i in range(1,6):
    print("Número:", i)

print("================================")

#Bucle for con lista 
habilidades =  ["Python", "Git", "Github", "VsCode"]
print("lo que ya aprendí")
for habilidad in habilidades:
    print("check", habilidad)

print("================================")

# Bucle while
print("=====Mi cuenta regresiva ======")
meses_restantes = 12
while meses_restantes > 0:
    print("Faltan", meses_restantes, "meses para mi meta")
    meses_restantes = meses_restantes - 1

print("¡Meta alcanzada! ¡Estoy listo para ser un developer!")