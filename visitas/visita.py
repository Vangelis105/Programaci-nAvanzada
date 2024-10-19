from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from random import randint
from typing import List
from datetime import date

class Visita: 
    id: str
    guia_a_cargo: Empleado
    costo_total: float
    visitantes: List[Visitante]=[]
    fecha_visita: date
    cantidad_adultos: int
    cantidad_niños: int

    def __init__(self, id:str,
                 guia_a_cargo: Empleado, 
                 costo_total: float,
                 visitantes: List[Visitante],
                 fecha_visita: date,
                 cantidad_adultos: int,
                 cantidad_niños: int):
        self.id = id
        self.guia_a_cargo = guia_a_cargo
        self.costo_total = costo_total
        self.visitantes = visitantes
        self.fecha_visita = fecha_visita
        self.cantidad_adultos = cantidad_adultos
        self.cantidad_niños = cantidad_niños

    
    def mostrar_info_visita(self):
        info = f"""
                ID de visita: {self.id}
                ID del guia a cargo: {self.guia_a_cargo.id} 
                Nombre de guia a cargo: {self.guia_a_cargo.nombre} {self.guia_a_cargo.apellidos}
                Fecha de realizacion de la visita: {self.fecha_visita}
                Costo total de visita: {self.costo_total}
                Cantidad de adultos: {self.cantidad_adultos}
                Cantidad de niños: {self.cantidad_niños}
                """
        return info
    
    def mostrar_visitantes(self):
        i=0
        print("\n---Visitantes---\n")
        for visitante in self.visitantes:
            i = i+1
            print("Visitante ", i)
            print("-ID: ", visitante.id)
            print("-Nombre: ", visitante.nombre, visitante.apellidos, "\n")
            
