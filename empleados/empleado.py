from datetime import time
from datetime import date
from empleados.utils.rol import Rol
from usuarios.usuario import Usuario
from random import randint

class Empleado(Usuario):
 
    fecha_inicio: date
    rfc: str
    salario: float
    horario: str
    rol: Rol
    disponible: bool

    def __init__(self, id: str, nombre: str, apellidos: str, fecha_nacimiento: date, fecha_inicio: date, rfc: str, curp: str, salario: float, horario: str, rol: Rol):
        super().__init__(id=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, curp=curp)
        self.fecha_inicio = fecha_inicio
        self.rfc = rfc
        self.salario = salario
        self.horario = horario
        self.rol = rol
        self.disponible = True


    def mostrar_info(self):
        nombre_completo= f"{self.nombre} {self.apellidos}"
        info=f"\n-ID: {self.id}\n-Nombre completo: {nombre_completo}\n-Fecha de nacimiento: {self.fecha_nacimiento}\n-Fecha de inicio: {self.fecha_inicio}\n-RFC: {self.rfc}\n-CURP: {self.curp}\n-Salario: {self.salario}\n-Horario: {self.horario}"
        return info