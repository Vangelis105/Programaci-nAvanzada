import random

class Paciente:
    id: int
    nombre: str
    ano_nacimiento: int
    peso: float
    estatura: float
    direccion: str

    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
        self.id = random.randint(1, 10001)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"\nId: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"Peso: {self.peso}")
        print(f"Estatura: {self.estatura}")
        print(f"Dirección: {self.direccion}")

    # @property
    # def id(self):
    #     return self.id
    
    # @property
    # def set_id(self, id):
    #     self.id = id
    
    # @property
    # def name(self):
    #     return self.name
    
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def peso(self):
    #     return self.peso
    
    # @property
    # def estatura(self):
    #     return self.estatura
    
    # @property
    # def direccion(self):
    #     return self.direccion