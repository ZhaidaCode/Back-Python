class EmpresaObjetivo:
    def __init__(self, name, country, area):
        self.name = name
        self.country = country
        self.area = area
        self. aplicada = False
    
    def aplicar (self):
        self.aplicada = True
        print(f'Aplicaste a:, {self.name}')

    def mostrar_estado(self):
        estado = "Aplicada" if self.aplicada else "No aplicada"
        print(f'Empresa: {self.name}, -  Estado: {estado}')

#Crear tus empresas objetivo
mercado_libre = EmpresaObjetivo("Mercado Libre", "Argentina", "E-commerce")
google = EmpresaObjetivo("Google", "Estados Unidos", "Tecnología")
amazon = EmpresaObjetivo("Amazon", "Estados Unidos", "E-commerce")

#Simular que aplicaste a Yape
mercado_libre.aplicar()

#Ver estado de todas
print("=== MIS EMPRESAS OBJETIVO ===")
mercado_libre.mostrar_estado()
google.mostrar_estado()