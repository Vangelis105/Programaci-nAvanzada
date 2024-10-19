from datetime import datetime
from animales.utils.alimentacion import Alimentacion
from typing import List
from random import randint

class Animal:

    id: str
    tipo: str
    fecha_llegada: datetime
    enfermedades: List[str] = []
    tipo_alimentacion: Alimentacion
    fecha_nacimiento: datetime
    peso: float
    frecuencia_alimentacion: str
    vacunas: bool

    def __init__(self, id:str, tipo:str, fecha_llegada: str, enfermedades: List[str], tipo_alimentacion: Alimentacion, fecha_nacimiento: datetime, peso:float, frecuencia_alimentacion: str, vacunas: bool ):
        self.id = id
        self.tipo = tipo
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacion = tipo_alimentacion
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.vacunas = vacunas
    
    def mostrar_info_animal(self):
        info = f"""Animal: {self.tipo.upper()}
                   ID: {self.id} 
                   Fecha de llegada: {self.fecha_llegada}
                   Enfermedades: {self.enfermedades}
                   Tipo de alimentacion: {self.tipo_alimentacion.value}
                   Frecuencia de alimentacion: {self.frecuencia_alimentacion}
                   Fecha de nacimiento: {self.fecha_nacimiento}
                   Peso: {self.peso} kg
                   Vacunado: {self.vacunas}"""
        return info
        
 