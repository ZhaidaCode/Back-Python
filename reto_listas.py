# Sistema simple de metas
metas_pendientes = ["Aprender listas", "Aprender dicccionarios", "Construir una api", "Conseguir trabajo tech"]
metas_completadas = []

#Completar la primera meta
primera_meta = metas_pendientes[0]
metas_completadas.append(primera_meta)
metas_pendientes.remove(primera_meta)

#Mostrar estado
print("=====MIS METAS=====")
print("Metas pendientes:")
for meta in metas_pendientes:
    print("⏳", meta)

print("Metas completadas:")
for meta in metas_completadas:
    print("✅", meta)

print("===================")
print("Pendientes:", len(metas_pendientes))
print("Completadas:", len(metas_completadas))