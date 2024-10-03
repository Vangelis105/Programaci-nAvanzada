from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    RFC: str
    años_antiguedad: int


    def __init__(self, numero_control: str, nombre:str, apellido:str, sueldo:float, RFC:str, años_antiguedad: int, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.COORDINADOR)
        self.sueldo = sueldo
        self.RFC = RFC
        self.años_antiguedad = años_antiguedad

