from datetime import datetime

class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    ano_nacimiento: datetime
    rfc: str
    sueldo: float

    def __init__(self, numero_control: str, nombre:str, apellido:str, ano_nacimiento: datetime, rfc:str, sueldo:float):
        self.numero_control = numero_control 
        self.nombre = nombre
        self.apellido = apellido
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo


