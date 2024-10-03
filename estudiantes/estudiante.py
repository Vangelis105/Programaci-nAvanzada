from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, numero_control:str, nombre:str, apellido:str, curp:str, fecha_nacimiento:datetime, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.ESTUDIANTE)
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_estudiante(self):
        nombreCompleto = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control}, nombre completo: {nombreCompleto.upper()}, curp: {self.curp.upper()}, fecha de nacimiento: {self.fecha_nacimiento}, rol: {self.rol.value}"
        return info
    


