from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_grupos: List[Grupo] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        print("Estudiante registrado correctamente")

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
        print("Maestro registrado correctamente")
        
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
        
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
                
        self.lista_semestres.append(semestre)
        
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
            
        self.lista_grupos.append(grupo)

    def listar_estudiantes(self):
        print("\n\t+++ ESTUDIANTES +++")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def listar_maestros(self):
        print("\n\t+++ MAESTROS +++")

        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())

    def listar_materias(self):
        print("\n\t+++ MATERIAS +++")

        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())

    def listar_grupos(self):
        print("\n\t+++ GRUPOS +++")
        
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
            
    def listar_carreras(self):
        print("\n\t+++ CARRERAS +++")
        
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
            
    def listar_semestres(self):
        print("\n\t+++ SEMESTRES +++")
        
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())
    
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove()
                print("Estudiante eliminado")
                return
            
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove()
                print("Maestro eliminado")
                return
        print("No se encontró un maestro con numero de control: ",numero_control)
        return
        
    def eliminar_materia(self, id: str):
        for materia in self.lista_materias:
            if materia.id == id:
                self.lista_materias.remove()
                print("Materia eliminado")
                return
        print("No se encontró una materia con ID: ",id)
        return



    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        print("Materia registrada correctamente")

    def generar_id_materia(self, nombre, semestre, creditos):
        id = f"MT{nombre[-2:].upper()}{semestre}{creditos}{randint(1, 1000)}"
        return id

    def generar_numeroControl_E(self):
        
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes)+1}{randint(0, 10000)}"
        return numero_control
    
    def generar_numeroControl_M(self, ano_nacimiento, nombre, rfc):

        numero_control = f"M{str(ano_nacimiento[-2:])}{datetime.now().day}{randint(500, 5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros)+1}"
        return numero_control
        