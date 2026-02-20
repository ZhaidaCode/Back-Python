# Operadores matemticos
precio = 100 
descuento  = 20
precio_final = precio - descuento

print("precio original:", precio)
print("descuento:", descuento)
print("precio final:", precio_final)

print("------------------------------")

# Condicionales
meses_estudiados = 6

if meses_estudiados >= 12:
    print("¡Lista para aplicar a Mercado Libre o Yape Tech!")
elif meses_estudiados >= 6:
    print("¡Vas por buen camino, sigue estudiando!")
elif meses_estudiados >= 1:
    print("Recien estás comenzando, ¡ánimo!")
else: print("¡Aún no has comenzado a estudiar, es hora de empezar!")