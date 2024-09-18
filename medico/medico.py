import random

class Medico:
    id: int
    nombre: str
    ano_nacimiento: int
    rfc: str
    direccion: str

    def __init__(self, nombre, ano_nacimiento, rfc, direccion):
        self.id = random.randint(1, 1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def mostrar_informacion_medico(self):
        print(f"\nId: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"RFC: {self.rfc}")
        print(f"Dirección: {self.direccion}")

    # @property
    # def id(self):
    #     return self.id
    
    # @property
    # def name(self):
    #     return self.name
    
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def rfc(self):
    #     return self.rfc
    
    # @property
    # def direccion(self):
    #     return self.direccion