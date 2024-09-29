from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia]
    grupos: List[Grupo]


    def __init__(self, numero:int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero
        self.grupos: List[Grupo] = []

    def generar_id(self, numero) -> str:
        return f"{numero}-{randint(0, 1000000)}-{randint(0, 100000)}"
    
    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)


    def mostrar_info_semestre(self):
        info = f"ID: {self.id}, numero: {self.numero}, ID de la carrera a la que pertenence: {self.id_carrera}"
        return info
