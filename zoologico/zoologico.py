from empleados.empleado import Empleado
from visitantes.visitantes import Visitante
from visitas.visita import Visita
from usuarios.usuario import Usuario
from typing import List
from datetime import datetime
from datetime import date
from empleados.utils.rol import Rol
from animales.animal import Animal
from director.director import Director
from random import randint
from animales.utils.alimentacion import Alimentacion
from procesos.proceso import Proceso
from procesos.utils.tipos_procesos import TiposProcesos

class Zoologico:
    lista_empleados:List[Empleado]=[]
    lista_usuario: List[Usuario]=[]
    lista_animales: List[Animal]=[]
    lista_visitantes: List[Visitante]=[]
    lista_visitas: List[Visita]=[]
    lista_procesos: List[Proceso]=[]
    director: Director
    

    def __init__(self):
        director=Director(id="NACO777", nombre="Vangelis", apellidos="Contreras", fecha_nacimiento=date(2004, 1, 23), curp="VCOM0104123HMNNLLA1", contraseña="105")
        self.director=director
        self.lista_usuario.append(director)

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        self.lista_usuario.append(visitante)

    def registrar_empleado(self, empleado: Empleado):
        self.lista_empleados.append(empleado)
        self.lista_usuario.append(empleado)
    
    def registrar_animal(self, animal: Animal):
        self.lista_animales.append(animal)
    
    def registrar_proceso(self, proceso: Proceso):
        self.lista_procesos.append(proceso)
    
    def capturar_tipo_alimentacion(self):   
        ciclo_alimentacion = 0
        while ciclo_alimentacion < 1 or ciclo_alimentacion >= 4:
            ciclo_alimentacion = int(input("Ingresa el tipo de alimentacion del animal: \n1. Herviboro \n2. Carnivoro \n3. Omnivoro \n: "))
            
            if ciclo_alimentacion == 1:
                tipo_alimentacion = Alimentacion.HERVIBORO
                return tipo_alimentacion
            elif ciclo_alimentacion == 2:
                tipo_alimentacion = Alimentacion.CARNIVORO
                return tipo_alimentacion
            elif ciclo_alimentacion == 3:
                tipo_alimentacion = Alimentacion.OMNIVORO
                return tipo_alimentacion
            else:
                print("Opcion invalida. Intenta de nuevo")
                
    def capturar_enfermedades(self):
        opcion_enfermedad = 0
        enfermedades = []
        while opcion_enfermedad <1 or opcion_enfermedad >=3:
            cuenta_con_enfermedad = int(input("Ingresa si el animal cuenta con enfermedades: \n1. Si \n2. No \n: "))
            if cuenta_con_enfermedad == 1:
                opcion_enfermedad = 0
                enfermedad = input("Ingresa la enfermedad del animal: ")
                enfermedades.append(enfermedad)
                while opcion_enfermedad != 2:
                    opcion_enfermedad = int(input("Agregar otra enfermedad. \n1. Si \n2. No \n: "))
                    if opcion_enfermedad == 1:
                        enfermedad = input("Ingresa la enfermedad del animal: ")
                        enfermedades.append(enfermedad)
                    elif opcion_enfermedad != 2: 
                        print("Opcion invalida. Intenta de nuevo")
                        
            elif cuenta_con_enfermedad == 2:
                break
            else:
                print("Opcion invalida. Intenta de nuevo")   
        if len(enfermedades) == 0:
            enfermedad = "Sin enfermedades"
            enfermedades.append(enfermedad)
            return enfermedades
        else:
            return enfermedades  
              
    def capturar_vacunas(self):  
        vacunado = 0
        while vacunado <1 or vacunado >=3:
            vacunado = int(input("El animal esta vacunado? \n1. Si \n2. No \n: " ))
            if vacunado == 1:
                vacunas = True
            elif vacunado == 2:
                vacunas = False
            else:
                print("Opción inválida. Intenta de nuevo.")       
        return vacunas           
    
    def mostrar_animales(self):
        print("\n*** ANIMALES EN EL ZOOLOGICO ***")
        cantidad_animales = 0
        for animal in self.lista_animales: 
            cantidad_animales =+ 1
            print(animal.mostrar_info_animal())
        if cantidad_animales == 0:
            print("NO HAY ANIMALES A MOSTRAR")
            return False
        else:
            return True
    
    def generar_id_animal(self, tipo, fecha_llegada, fecha_nacimiento):
        id = f"AN{tipo[:2].upper()}{str(fecha_llegada.year)[-2:]}{str(fecha_llegada.month)}{randint(1, 10000)}{datetime.now().day}{str(fecha_nacimiento.year)[-2:]}"
        for animal in self.lista_animales:
            while id == animal.id:
                print("El ID estaba duplicado, generando nuevo...")
                id = f"AN{tipo[:2].upper()}{str(fecha_llegada.year)[-2:]}{str(fecha_llegada.month)}{randint(1, 10000)}{datetime.now().day}{str(fecha_nacimiento.year)[-2:]}"
        return id
    
    def generar_id_empleado(self, nombre: str, rol: Rol, fecha_inicio: date, rfc:str):
        iniciales_nombre=nombre[0:3].upper()
        id=f"{iniciales_nombre}{str(rol.value)[:2].upper()}{randint(0,5000)}{str(fecha_inicio.year)[-2:]}{rfc[:2].upper()}"
        for empleado in self.lista_empleados:
            while id == empleado.id:
                print("El ID estaba duplicado, generando nuevo... ")
                iniciales_nombre=nombre[0:3].upper()
                id=f"{iniciales_nombre}{str(rol.value)[:2].upper()}{randint(0,5000)}{str(fecha_inicio.year)[-2:]}{rfc[:2].upper()}"
        return id
    
    def generar_id_visitante(self, nombre: str, apellidos: str, fecha_nacimiento:date, fecha_registro:date):
        iniciales_nombre=nombre[:2].upper()
        iniciales_apellidos=apellidos[:2].upper()
        id=f"{iniciales_nombre}{iniciales_apellidos}{randint(0, 10000)}{str(fecha_nacimiento.year)[-2:]}{str(fecha_registro.year)[-2:]}"
        for visitante in self.lista_visitantes:
            while id == visitante.id:
                print("El ID estaba duplicado, generando nuevo...")
                iniciales_nombre=nombre[:2].upper()
                iniciales_apellidos=apellidos[:2].upper()
                id=f"{iniciales_nombre}{iniciales_apellidos}{randint(0, 10000)}{str(fecha_nacimiento.year)[-2:]}{str(fecha_registro.year)[-2:]}"
        return id
    
    def generar_id_visita (self, guia_a_cargo: Empleado, fecha_visita:date):
        nombre = guia_a_cargo.nombre
        id = f"{nombre[:2].upper()}{randint(0,10000)}{str(fecha_visita.year)[-2:]}{randint(0,10000)}"
        for visita in self.lista_visitas:
            while id == visita.id:
                print(" El ID estaba duplicado, generando nuevo...")
                nombre = guia_a_cargo.nombre
                id = f"{nombre[:2].upper()}{randint(0,10000)}{str(fecha_visita.year)[-2:]}{randint(0,10000)}"
        return id

    
    def mostrar_procesos(self):    
        print("\n--- Procesos realizados ---")
        for proceso in self.lista_procesos:
            print(proceso.mostrar_info_proceso())

    def mostrar_visitas(self):    
        print("\n--- Visitas realizadas ---")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visita())
            visita.mostrar_visitantes()
           
    def mostrar_veterinarios(self):
        print("\n---VETERINARIOS---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.VETERINARIO:
                print(empleado.mostrar_info())
    
    def mostrar_administracion(self):
        print("\n---ADMINISTRADORES---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.ADMINISTRACION:
                print(empleado.mostrar_info())
    
    def mostrar_mantenimiento(self):
        print("\n---ENCARGADOS DE MANTENIMIENTO---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.MANTENIMIENTO:
                print(empleado.mostrar_info())
                
    def mostrar_mantenimiento_disponible(self):
        print("\n---ENCARGADOS DE MANTENIMIENTO DISPONIBLES---\n")
        numero_disponibles = 0
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.MANTENIMIENTO:
                if empleado.disponible == True:
                    print(empleado.mostrar_info())
                    numero_disponibles =+ 1
        if numero_disponibles == 0:
            print("NO HAY EMPLEADOS DE MANTENIMIENTO DISPONIBLES")
            return False
        else:
            return True
    
    def comprobrar_existencia_empleados(self):
        if self.lista_empleados==[]:
            print("\nNO EXISTEN EMPLEADOS\n")
            return False
        else:
            return True
    
    def mostrar_guia(self):
        print("\n---GUIAS---\n")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.GUIA:
                print(empleado.mostrar_info())

    def mostrar_guia_disponibles(self):
        disponibilidad = 0
        print("\n---GUIAS DISPONIBLES---")
        for empleado in self.lista_empleados:
            if empleado.rol == Rol.GUIA:
                if empleado.disponible == True:
                    print(empleado.mostrar_info())
                    disponibilidad += 1
        if disponibilidad == 0:
            print("\nNO HAY GUIAS DISPONIBLES\n")
            return False
        else:
            return True

    def mostrar_visitantes(self):
        print("\n---VISITANTES---\n")
        for visitantes in self.lista_visitantes:
            print(visitantes.mostrar_info_visitante())
    
    def registrar_visita(self, visita: Visita):
        self.lista_visitas.append(visita)

    def revision_visitantes(self, visitantes:List[Visitante]=[]):
        precio = 0
        adultos= 0
        niños = 0
        for visitante in visitantes:
            if (datetime.now().year - visitante.fecha_nacimiento.year) < 18:
                niños+=1
                if visitante.numero_visitas == 6:
                    precio = precio + (50 * 0.8)
                    visitante.numero_visitas = 0
                else:
                    precio = precio + 50
            else:
                adultos+=1
                if visitante.numero_visitas == 6:
                    precio = precio + (100 * 0.8)
                    visitante.numero_visitas = 0
                else:
                    precio = precio + 100

        return precio, adultos, niños
                    
    def validar_id(self, id:str):
        for visitante in self.lista_visitantes:
            if id == visitante.id:
                visitante.numero_visitas = visitante.numero_visitas + 1
                return visitante
        print("\nID no encontrada")
        return None
                
    def validar_id_animal(self, id_animal:str):
        for animal in self.lista_animales:
            if id_animal == animal.id:
               return id_animal
            else:
                print("El ID es incorrecto") 
        return None
        

    def validar_id_guia(self, id_guia:str):
        for empleado in self.lista_empleados:
            if id_guia == empleado.id:
                if empleado.rol == Rol.GUIA:
                    if empleado.disponible == True:
                        empleado.disponible = False
                        return empleado
        print("\nID no encontrada o guia no disponible")
        print("Vuelva a intentarlo")
        return None
    
    def validar_id_empleado(self, id_empleado:str):
        for empleado in self.lista_empleados:
            if id_empleado == empleado.id:
                return id_empleado
        print("\nID no encontrada")
        print("Vuelva a intentarlo")
        return None
        
    def validar_id_encargado(self, id_encargado:str):
        for empleado in self.lista_empleados:
            if id_encargado == empleado.id:
                if empleado.rol == Rol.MANTENIMIENTO:
                    empleado.disponible = False
                    return empleado
                else: 
                    print("El empleado no es de mantenimiento")
         
        print("ID no encontrada")

    def verificar_id_y_contraseña(self, id_ingresada: str, contraseña_ingresada: str):
        if contraseña_ingresada == self.director.contraseña and id_ingresada == self.director.id:
            return True
        return False
    
    def seleccion_tipo_proceso(self):
        opcion_proceso = 0
                
        while opcion_proceso <1 or opcion_proceso >= 4:
            
            print("1. Mantenimiento")
            print("2. Alimentacion")
            print("3. Limpieza")
            opcion_proceso = int(input("Selecciona el tipo de proceso a registrar: "))
            
            if opcion_proceso == 1:
                tipo_proceso = TiposProcesos.MANTENIMIENTO
                return tipo_proceso
            elif opcion_proceso == 2:
                tipo_proceso = TiposProcesos.ALIMENTACION
                return tipo_proceso
            elif opcion_proceso == 3:
                tipo_proceso = TiposProcesos.LIMPIEZA
                return tipo_proceso
            else:
                print("Opcion invalida. Intenta de nuevo")
    
    def observaciones(self):                 
        registrar_observaciones = 0
        while registrar_observaciones !=2 :    
            print("Desea ingresar observaciones?")
            print("\n1. Si \n2. No")
            registrar_observaciones = int(input(": "))
            if registrar_observaciones == 1:
                observaciones = input("Escribe tus observaciones: ")
                return observaciones
            elif registrar_observaciones == 2:
                observaciones = None
                return observaciones
            else:
                print("Opcion no valida")    
    
    def seleccion_tipo_proceso(self):
        opcion_proceso = 0
                
        while opcion_proceso <1 or opcion_proceso >= 4:
            
            print("1. Mantenimiento")
            print("2. Alimentacion")
            print("3. Limpieza")
            opcion_proceso = int(input("Selecciona el tipo de proceso a registrar: "))
            
            if opcion_proceso == 1:
                tipo_proceso = TiposProcesos.MANTENIMIENTO
                return tipo_proceso
            elif opcion_proceso == 2:
                tipo_proceso = TiposProcesos.ALIMENTACION
                return tipo_proceso
            elif opcion_proceso == 3:
                tipo_proceso = TiposProcesos.LIMPIEZA
                return tipo_proceso
            else:
                print("Opcion invalida. Intenta de nuevo")
    
    def observaciones(self):           
                    
        registrar_observaciones = 0
        while registrar_observaciones !=2 :    
            print("Desea ingresar observaciones?")
            print("\n1. Si \n2. No")
            registrar_observaciones = int(input(": "))
            if registrar_observaciones == 1:
                observaciones = input("Escribe tus observaciones: ")
                return observaciones
            elif registrar_observaciones == 2:
                observaciones = None
                return observaciones
            else:
                print("Opcion no valida")

    def modificar_empleado(self, id_empleado):
        for empleado in self.lista_empleados:
            if id_empleado == empleado.id:
                while True:
                    print("\nSelecciones atributo a modificar: \n")
                    print("1. Nombre")
                    print("2. Apellidos")
                    print("3. Salario")
                    print("4. RFC")
                    print("5. CURP")
                    print("6. Horario")
                    print("7. Rol")
                    print("8. Cancelar")

                    opcion=input("\nIngrese una opcion: ")

                    if opcion == "1":
                        empleado.nombre=input("Ingrese el nuevo nombre: ")
                    elif opcion == "2":
                        empleado.apellidos=input("Ingrese los nuevos apellidos: ")
                    elif opcion == "3":
                        empleado.salario=float(input("Ingrese el nuevo salairo: "))
                    elif opcion == "4":
                        empleado.rfc=input("Ingrese el nuevo RFC: ")
                    elif opcion == "5":
                        empleado.curp=input("Ingrese la nueva CURP: ")
                    elif opcion == "6":
                        hora_entrada=input("Ingrese la nueva hora de entrada: ")
                        hora_salida=input("Ingrese la nueva hora de salida: ")
                        horario=f"{hora_entrada} a {hora_salida}"
                        empleado.horario=horario
                    elif opcion == "7":
                        if empleado.rol == Rol.GUIA:
                            for visita in self.lista_visitas:
                                if id_empleado == visita.guia_a_cargo.id:
                                    print("\nEste guia tiene una visita asociada, no es posible modificar su rol\n")
                                    return
                            print("Roles a seleccionar\n")
                            print("1. Administraion\n2. Mantenimiento\n3. Veterinario\n")
                            rol_nuevo=input("Selecciones rol: ")
                            if rol_nuevo=="1":
                                empleado.rol=Rol.ADMINISTRACION
                            elif rol_nuevo=="2":
                                empleado.rol=Rol.MANTENIMIENTO
                            elif rol_nuevo=="3":
                                empleado.rol=Rol.VETERINARIO
                            else:
                                print("Rol no valido")
                        else:
                            for proceso in self.lista_procesos:
                                if id_empleado == proceso.empleado_encargado.id:
                                    print("\nEste empleado esta relacionado a un proceso, no es posible modificar su rol\n")
                                    return
                            print("Seleccione el nuevo rol: ")
                            print("1. Administraion\n2. Guia\n3. Veterinario\n4. Mantenimiento")
                            rol_nuevo=input("Selecciones rol: ")
                            if rol_nuevo=="1":
                                empleado.rol=Rol.ADMINISTRACION
                            elif rol_nuevo=="2":
                                empleado.rol=Rol.GUIA
                            elif rol_nuevo=="3":
                                empleado.rol=Rol.VETERINARIO
                            elif rol_nuevo=="4":
                                empleado.rol=Rol.MANTENIMIENTO
                            else:
                                print("Rol no valido")
                    elif opcion=="8":
                        break
                    else:
                        print("\nOpcion no valida\n")
                return
                
                            
    def modificar_animal(self, id_modificar:str):
        for animal in self.lista_animales:
            if id_modificar == animal.id:
                
                while True:
                    print("\n1. Tipo de animal \n2. Enfermedades \n3. Tipo de alimentacion \n4. Fecha de nacimiento \n5. Peso \n6. Frecuencia de alimentacion \n7. Vacunas con las que cuenta \n8. Salir") 
                    opcion = int(input("Ingresa la opcion de lo que desees modificar [No se permite modificar el ID o fecha de llegada (registro) del animal]: "))
                    if opcion == 1:
                        animal.tipo = input("Ingresa el nuevo tipo/especie de animal: ")
                        print("Modificacion realizada con exito")
                        
                    elif opcion == 2:
                        animal.enfermedades = self.capturar_enfermedades()
                        print("Modificacion realizada con exito")
                        
                    elif opcion == 3:
                        animal.tipo_alimentacion = self.capturar_tipo_alimentacion()
                        print("Modificacion realizada con exito")
                        
                    elif opcion == 4:
                        dia_nacimiento = int(input("Ingresa el dia de nacimiento del animal: "))
                        mes_nacimiento = int(input("Ingresa el mes de nacimiento del animal: "))
                        año_nacimiento = int(input("Ingresa el año de nacimiento del animal: "))
                        animal.fecha_nacimiento = datetime.date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                        print("Modificacion realizada con exito")

                    elif opcion == 5:
                        animal.peso = float(input("Ingresa el peso en kg del animal: "))
                        print("Modificacion realizada con exito")
                    
                    elif opcion == 6:
                        animal.frecuencia_alimentacion = input("Ingresa la frecuencia de alimentacion del animal: ")
                        print("Modificacion realizada con exito")
                       
                    elif opcion == 7:
                        animal.vacunas = self.capturar_vacunas()
                        print("Modificacion realizada con exito")
                    elif opcion == 8:
                        print("Saliste de modificaciones de animal")
                        break
                    else:
                        print("Opcion no valida. Intente de nuevo")
                return       
        print("ID no encontrado")
        
                
    def eliminar_animal(self, id_eliminar: str):
    
        for animal in self.lista_animales:
            if animal.id == id_eliminar:
                for proceso in self.lista_procesos:
                    if proceso.id_animal == animal.id:
                        print("No se puede eliminar el animal debido a que está asociado con un proceso")
                        return
                self.lista_animales.remove(animal)
                print("Animal eliminado con éxito")
                return
        print("No se ha encontrado el ID del animal")
    
    def eliminar_empleado(self, id_empleado: str):
        for empleado in self.lista_empleados:
            if id_empleado == empleado.id:
                if empleado.rol == Rol.GUIA:
                    for visita in self.lista_visitas:
                        if visita.guia_a_cargo.id == id_empleado:
                            print("\nNo se puede eliminar el empleado debido a que esta asociado a una visita")
                            return
                    self.lista_empleados.remove(empleado)
                    print("\nEmpleado eliminado")

                elif empleado.rol == Rol.MANTENIMIENTO:
                    for proceso in self.lista_procesos:
                        if proceso.empleado_encargado.id == id_empleado:
                            print("No se puede elimianr el empleado debido a que tiene un proceso asociado")
                            return
                    self.lista_empleados.remove(empleado)
                    print("\nEmpleado eliminado")
                else:
                    self.lista_empleados.remove(empleado)
                    print("\nEmpleado eliminado")

    def eliminar_visitante(self, id: str):
        for visita in self.lista_visitas:
            for visitante in visita.visitantes:
                if id == visitante.id:
                    print("\nNo es posible eliminar el visiante porque ya tiene una visita asociada\n")
                    return
        
    def modificar_visitante(self, id_modificar:str):
        for visitante in self.lista_visitantes:
            if visitante.id == id_modificar:
                while True:
                    print("\n1. Nombre \n2. Apellidos \n3. Fecha de nacimiento \n3. CURP \n4. Salir") 
                    opcion = int(input("Ingresa la opcion de lo que desees modificar [No se permite modificar el ID, numero de visitas ni fechas de registro o nacimiento]: "))
                    
                    if opcion == 1:
                        visitante.nombre = input("Ingresa el nombre del visitante: ")
                        print("Modificacion realizada con exito")
                    elif opcion == 2:
                        visitante.apellidos = input("Ingresa los apellidos del visitante: ")
                        print("Modificacion realizada con exito")
                    elif opcion == 3:
                        visitante.curp = input("Ingresa la CURP: ")
                        print("Modificacion realizada con exito")
                    elif opcion == 4:
                        print("Saliste de modificaciones del visitante")    
                        break
                    else: 
                        print("Opcion no válida. Intenta de nuevo")
                return
        print("ID no encontrado")        
                    
                    
