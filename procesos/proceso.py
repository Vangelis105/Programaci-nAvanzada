from empleados.empleado import Empleado
from procesos.utils.tipos_procesos import TiposProcesos
from datetime import date

class Proceso:
    empleado_encargado: Empleado
    tipo_proceso: TiposProcesos
    observaciones: str
    fecha_proceso: date
    id_animal: str
    
    def __init__(self, empleado_encargado: Empleado, tipo_proceso: TiposProcesos, observaciones: str, fecha_proceso: date, id_animal:str):
        self.empleado_encargado = empleado_encargado
        self.tipo_proceso = tipo_proceso
        self.observaciones = observaciones
        self.fecha_proceso = fecha_proceso
        self.id_animal = id_animal
        
    def mostrar_info_proceso(self):
        info = f"""
                Tipo de proceso: {self.tipo_proceso.value}
                ID del animal: {self.id_animal} 
                Empleado encargado: {self.empleado_encargado.nombre}
                ID del empleado encargado: {self.empleado_encargado.id}
                Fecha de realizacion del proceso: {self.fecha_proceso}
                Observaciones: {self.observaciones}
                """
        return info