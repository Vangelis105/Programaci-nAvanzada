from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    ano_nacimiento: datetime
    rfc: str
    sueldo: float

    def __init__(self, numero_control: str, nombre:str, apellido:str, ano_nacimiento: datetime, rfc:str, sueldo:float, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.MAESTRO)
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombreCompleto = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control}, nombre completo: {nombreCompleto.upper()}, año de nacimiento: {self.ano_nacimiento}, rfc: {self.rfc}, sueldo por hora: ${self.sueldo}, rol: {self.rol.value}"
        return info


