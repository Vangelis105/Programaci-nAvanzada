from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materia] = []
    tipo: str
    id_semestre: int
    
    
    def __init__(self, tipo: str, id_semestre: str):
        self.id = self.generar_id(tipo)
        self.tipo = tipo
        self.id_semestre = id_semestre


    def generar_id(self, tipo: str) -> str:
        return f"{tipo}-{randint(0, 1000000)}-{randint(0, 100000)}"
    
    def mostrar_info_grupo(self):
        info = f"ID: {self.id}, tipo: {self.tipo}, ID del semestre: {self.id_semestre}"
        return info
    
    