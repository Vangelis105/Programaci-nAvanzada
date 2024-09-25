from datetime import datetime

class Estudiante:
    numero_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, numero_control:str, nombre:str, apellido:str, curp:str, fecha_nacimiento:datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_estudiante(self):
        nombreCompleto = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control}, nombre completo: {nombreCompleto.upper()}, curp: {self.curp.upper()}, fecha de nacimiento: {self.fecha_nacimiento}"
        return info
    


