from .utils.roles import Rol

class Usuario:
    nombre: str
    numero_control: str
    apellido: str
    contraseña: str
    rol: Rol


    def __init__(self, numero_control:str, nombre: str, apellido: str, contraseña: str, rol:Rol):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.rol = rol
        
 