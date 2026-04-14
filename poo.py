class Developer:

    def __init__(self, name, country, goal):
        self.name = name
        self.country = country
        self.goal = goal
        self.skills = []
        self.months_of_study = 0

    def agregar_habilidad(self, skill):
        self.skills.append(skill)
        print(f'Habilidad agregada: "{skill}"')

    def study_mounth(self):
        self.months_of_study += 1
        print(f"Mes de estudio: {self.months_of_study}")

    def watch_perfil(self):
        print(f'{self.name}')
        print(f'País:, {self.country}')
        print(f'Meta: {self.goal}')
        print(f'Habilidades:')
        for h in self.skills:
            print("√", h)
        print(f'Total:, {len(self.skills)}, habilidades')

#Crear tu objeto
zhaida = Developer("Zhaida", "Perú", "Ser desarrolladora de backend en Mercado Libre")

#Agregar habilidades
zhaida.agregar_habilidad("Python")
zhaida.agregar_habilidad("Git")
zhaida.agregar_habilidad("Github")
zhaida.agregar_habilidad("listas")
zhaida.agregar_habilidad("diccionarios")
zhaida.agregar_habilidad("funciones")
zhaida.agregar_habilidad("Manejo de errores")

#Simular meses estudiados
zhaida.study_mounth()

#Mostrar perfil
zhaida.watch_perfil()

