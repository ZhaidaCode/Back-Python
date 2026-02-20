# Calculadora de tu meta developer
meses_para_meta = 12
meses_estudiados = 1
meses_restantes = meses_para_meta - meses_estudiados
porcentaje_avance = (meses_estudiados / meses_para_meta) * 100

print("==========MI PROGRESO HACIA MI META DE DEVELOPER==========")
print("Meses para alcanzar la meta:", meses_para_meta)
print("Meses estudiados:", meses_estudiados)
print("Meses restantes:", meses_restantes)
print("Porcentaje de avance:", porcentaje_avance, "%")
print("===========================================================")    

if porcentaje_avance >= 100:
    print("Estado: Meta cumplida")
elif porcentaje_avance >= 50:
    print("Estado: mas de la mitad, no pares")
elif porcentaje_avance >= 25:
    print("Estado: un cuarto del camino, sigue adelante")
else:    print("Estado: apenas comenzando, ¡ánimo!")

print("===========================================================")