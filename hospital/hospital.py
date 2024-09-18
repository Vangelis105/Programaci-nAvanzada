from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta


class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def eliminar_paciente(self, id_paciente_eliminar):
        print("\n *** Eliminar paciente ***")
        for paciente in self.pacientes:
            if paciente.id == id_paciente_eliminar:
                self.pacientes.remove(paciente)
                print("Se elimino el paciente con el ID: ",id_paciente_eliminar)
                
    def eliminar_medico(self, id_medico_eliminar):
        print("\n *** Eliminar medico ***")
        for medico in self.medicos:
            if medico.id == id_medico_eliminar:
                self.medicos.remove(medico)
                print("Se elimino el medico con el ID: ",id_medico_eliminar)

    def mostrar_pacientes(self):
        print("\n*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
            
    def mostrar_pacientes_menores(self):
        print("\n*** Pacientes en el Sistema menores de edad***")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) < 18:
                paciente.mostrar_informacion()
            
    def mostrar_pacientes_mayores(self):
        print("\n*** Pacientes en el Sistema mayores de edad***")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) > 17:
                paciente.mostrar_informacion()
        
    def mostrar_medicos(self):
        print("\n*** Medicos en el Sistema ***")
        for medico in self.medicos:
            medico.mostrar_informacion_medico()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True
