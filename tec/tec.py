from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_grupos: List[Grupo] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        print("Estudiante registrado correctamente")

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
        print("Maestro registrado correctamente")

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        print("Materia registrada correctamente")

    def generar_id_materia(self, nombre, semestre, creditos):
        id = f"MT{nombre[-2:].upper()}{semestre}{creditos}{randint(1, 1000)}"
        return id

    def generar_numeroControl_E(self):
        #L-2024-09-longitud lista estudiantes + 1-random
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes)+1}{randint(0, 10000)}"
        return numero_control
    
    def generar_numeroControl_M(self, ano_nacimiento, nombre, rfc):

        numero_control = f"M{str(ano_nacimiento[-2:])}{datetime.now().day}{randint(500, 5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros)+1}"
        return numero_control
        