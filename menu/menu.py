from zoologico.zoologico import Zoologico
from empleados.empleado import Empleado
from director.director import Director
from visitantes.visitantes import Visitante
from datetime import date
from datetime import time
from datetime import datetime
from empleados.utils.rol import Rol
from animales.animal import Animal
from typing import List
from visitas.visita import Visita
from procesos.proceso import Proceso

class Menu:
    zoologico = Zoologico()
    
    def login(self):
        intentos= 0
        print("\n---Binvenido al Zoologico de Morelia---\n")
        while intentos < 3:
            print("Inicia sesión para continuar\n")
            id_ingresada = input("Ingrese su ID: ").upper()
            contraseña_ingresada= input("Ingrese su contraseña: ")
            if self.zoologico.verificar_id_y_contraseña(id_ingresada=id_ingresada, contraseña_ingresada=contraseña_ingresada) == True:
                print("Inicio de sesión correcto")
                self.mostrar_menu()
            else:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)

        print("Máximos intentos de inicio de sesión alcanzados. Adiós\n")
        
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nID o contraseña incorrectos. Intenta de nuevo\n")
        return intentos_usuario + 1
    
    def mostrar_menu(self):
        while True:
            print("\n---BIENVENIDO---\n")
            print("Selecciona una opcion\n")
            print("1. Registrar empleado")
            print("2. Registrar visita")
            print("3. Registrar animal")
            print("4. Registrar proceso")
            print("5. Consultar visitantes")
            print("6. Consultar empleados")
            print("7. Consultar animales")
            print("8. Consultar procesos")
            print("9. Consultar visita")
            print("10. Modificar animales")
            print("11. Modificar empleado")
            print("12. Modificar visitantes")
            print("13. Eliminar animales")
            print("14. Eliminar empleados")
            print("15. Eliminar visitantes")
            print("16. Salir")
            
            opcion=input("Opcion: ")

            
            if opcion == "1":
                print("\nSeleccionaste registrar empleado\n")
            
                registrar = 0 
                
                while registrar < 1 or registrar >= 5:
                    print("\nSelecciona el tipo de empleado a registrar\n")
                    print("1. Administrador")
                    print("2. Mantenimiento")
                    print("3. Veterinario")
                    print("4. Guia")
                    
                    registrar= int(input("Tipo de empleado a registrar: "))
                    
                    if registrar ==1:
                        rol=Rol.ADMINISTRACION
                    elif registrar == 2:
                        rol=Rol.MANTENIMIENTO
                    elif registrar == 3:
                        rol=Rol.VETERINARIO
                    elif registrar == 4:
                        rol=Rol.GUIA
                    else:
                        print("\nOpcion no valida vuelva a intentar\n")                   
               
                nombre=input("Ingresa el nombre: ")
                apellidos=input("Ingresa los apellidos: ")
                dia_nacimiento=int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento=int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento=int(input("Ingresa el año de nacimiento: "))
                dia_inico=int(input("Ingresa el dia de inicio: "))
                mes_inicio=int(input("Ingresa el mes de inicio: "))
                año_incio=int(input("Ingresa el año de inicio: "))
                curp=input("Ingresa la curp: ")
                rfc=input("Ingresa RFC: ")
                salario=float(input("Ingresa el salario: "))
                hora_entrada=input("Ingrese la hora de entrada: ")
                hora_salida=input("Ingrese la hora de salida: ")

                fecha_nacimiento=date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                fecha_inicio=date(año_incio, mes_inicio, dia_inico)
                horario=f"{hora_entrada} a {hora_salida}"
                id=self.zoologico.generar_id_empleado(nombre=nombre, rol=rol, fecha_inicio=fecha_inicio, rfc=rfc)

                empleado=Empleado(id=id,
                                        nombre=nombre,
                                        apellidos=apellidos,
                                        fecha_nacimiento=fecha_nacimiento,
                                        fecha_inicio=fecha_inicio,
                                        rfc=rfc,
                                        curp=curp,
                                        salario=salario,
                                        horario=horario,
                                        rol=rol)
                    
                self.zoologico.registrar_empleado(empleado=empleado)
            
            elif opcion == "2":
                visitantes=[]
                guia = None
                print("\nSelecionaste la opción de registrar visita")
                print("\nBoleto adulto: $100.00")
                print("\nBoleto niño: $50.00")
                
                if self.zoologico.mostrar_guia_disponibles() == True:
                    while guia == None:
                        id_guia = input("\nIngresa el ID del guia para esta visita: ")
                        guia = self.zoologico.validar_id_guia(id_guia=id_guia)
                else:
                    continue
                fecha_visita=date.today()

                cantidad_visitantes = int(input("\n¿Cuantos visitantes desea registrar?: "))
                
                while cantidad_visitantes > 0:

                    nuevo = input("\n¿Eres nuevo visitante? (S/N): ").upper()
                    if nuevo == "S":
                        nombre=input("Ingresa el nombre: ")
                        apellidos=input("Ingresa los apellidos: ")
                        dia_nacimiento=int(input("Ingresa el dia de nacimiento: "))
                        mes_nacimiento=int(input("Ingresa el mes de nacimiento: "))
                        año_nacimiento=int(input("Ingresa el año de nacimiento: "))
                        curp=input("Ingresa la curp: ")
                        numero_visitas=0
                        fecha_registro=datetime.today()
                        fecha_nacimiento=date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                        id=self.zoologico.generar_id_visitante(nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, fecha_registro=fecha_registro)


                        visitante=Visitante(id=id, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento, curp=curp, numero_visitas=numero_visitas, fecha_registro=fecha_registro)
                        visitante.numero_visitas = visitante.numero_visitas + 1
                        self.zoologico.registrar_visitante(visitante=visitante)
                        
                        cantidad_visitantes = cantidad_visitantes - 1
                        visitantes.append(visitante)
                       
                    elif nuevo == "N":
                        visitante = None
                        while visitante == None:   
                            id = input("\n Ingresa tu ID: ")
                            visitante = self.zoologico.validar_id(id)
                            if visitante != None:   
                                cantidad_visitantes = cantidad_visitantes - 1
                                visitantes.append(visitante)
                                
                costo_total, adultos, niños = self.zoologico.revision_visitantes(visitantes=visitantes)
                
                print("\nPrecio total a pagar: ", costo_total)

                id=self.zoologico.generar_id_visita(guia_a_cargo=guia, fecha_visita=fecha_visita)

                visita = Visita(id=id, guia_a_cargo=guia, costo_total=costo_total, visitantes=visitantes, fecha_visita=fecha_visita, cantidad_adultos=adultos,cantidad_niños=niños)
                
                self.zoologico.registrar_visita(visita=visita)

            elif opcion == "3":
                print("\nSeleccionaste registrar un animal\n")
                tipo = input("Ingresa el tipo/especie de animal: ")
                peso = float(input("Ingresa el peso en kg del animal: "))
                fecha_llegada = date.today()
                dia_nacimiento = int(input("Ingresa el dia de nacimiento del animal: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento del animal: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento del animal: "))
                fecha_nacimiento = date(año_nacimiento, mes_nacimiento, dia_nacimiento)
                tipo_alimentacion = self.zoologico.capturar_tipo_alimentacion()
                frecuencia_alimentacion = input("Ingresa la frecuencia de alimentacion del animal: ")
                enfermedades = self.zoologico.capturar_enfermedades()
                vacunas = self.zoologico.capturar_vacunas()
                
                id = self.zoologico.generar_id_animal(tipo=tipo, fecha_llegada=fecha_llegada, fecha_nacimiento=fecha_nacimiento) 
    
                animal = Animal(id=id, tipo=tipo, fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animal(animal=animal)
                self.zoologico.mostrar_animales()
                
            elif opcion == "4":
                print("*** Registrar proceso ***")
                
                tipo_proceso = self.zoologico.seleccion_tipo_proceso()
                self.zoologico.mostrar_mantenimiento_disponible()
                if self.zoologico.mostrar_mantenimiento_disponible() == True:
                    id_encargado = input("Ingresa el ID del empleado a encargarse: ")
                    empleado_encargado = self.zoologico.validar_id_encargado(id_encargado=id_encargado)
                    
                    while empleado_encargado == None:
                        print("No se ha podido registrar el guia, intenta de nuevo")
                        id_encargado = input("Ingresa el ID del empleado a encargarse: ")
                        empleado_encargado = self.zoologico.validar_id_encargado(id_encargado=id_encargado)
                else:
                    continue
                
                if self.zoologico.mostrar_animales() == True:
                    id_animal = input("\nIngresa el ID del animal para realizar mantenimiento: ").upper()
                    id_animal = self.zoologico.validar_id_animal(id_animal=id_animal)
                    while id_animal == None:
                        print("No se ha podido registrar el animal, intenta de nuevo")
                        id_animal = input("\nIngresa el ID del animal para realizar mantenimiento: ").upper()
                        id_animal = self.zoologico.validar_id_animal(id_animal=id_animal)
                else:
                    continue
                
                observaciones = self.zoologico.observaciones()
                fecha_proceso = date.today()
                proceso = Proceso(empleado_encargado=empleado_encargado, tipo_proceso=tipo_proceso, observaciones=observaciones, fecha_proceso=fecha_proceso, id_animal=id_animal)
                self.zoologico.registrar_proceso(proceso=proceso)
            
            elif opcion == "5":
                self.zoologico.mostrar_visitantes()

            elif opcion == "6":
                print("\nSeleccionaste consultar empleado\n")
            
                consultar = 0 
                
                while consultar < 1 or consultar >= 5:
                    print("\nSelecciona el tipo de empleado a consultar\n")
                    print("1. Administrador")
                    print("2. Mantenimiento")
                    print("3. Veterinario")
                    print("4. Guia")
                
                    consultar= int(input("Tipo de empleado a consultar: "))

                    if consultar == 1:
                        self.zoologico.mostrar_administracion()
                    elif consultar == 2:
                        self.zoologico.mostrar_mantenimiento()
                    elif consultar == 3:
                        self.zoologico.mostrar_veterinarios()
                    elif consultar == 4:
                        self.zoologico.mostrar_guia()
                    else: 
                        print("Opcion no valida. Intente de nuevo")
            
            elif opcion == "7":
                self.zoologico.mostrar_animales()  
            
            elif opcion =="8":
                self.zoologico.mostrar_procesos()

            elif opcion == "9":
                self.zoologico.mostrar_visitas()
            
            elif opcion == "10":
                print("*** MODIFICAR ANIMALES ***")
                self.zoologico.mostrar_animales()
                id_modificar = input("Ingresa el ID del animal a modificar: ")
                self.zoologico.modificar_animal(id_modificar=id_modificar)
            
            elif opcion == "11":
                id=None
                print("\nSeleccionaste modifcar empleado\n")

                if self.zoologico.comprobrar_existencia_empleados() == True:

                    print("Lista de empleados registrados: \n")
                    self.zoologico.mostrar_administracion()
                    self.zoologico.mostrar_mantenimiento()
                    self.zoologico.mostrar_veterinarios()
                    self.zoologico.mostrar_guia()

                    while id==None:
                        id=input("Ingrese el ID del empleado a modificar: ")
                        id=self.zoologico.validar_id_empleado(id)
                else:
                    continue

                self.zoologico.modificar_empleado(id_empleado=id)
            
            elif opcion == "12":
                print("\n*** MODIFICAR VISITANTE ***\n")
                self.zoologico.mostrar_visitantes()
                id_modificar = input("Ingresa el ID del visitante a modificar: ")
                self.zoologico.modificar_visitante(id_modificar=id_modificar)

            elif opcion =="13":
                print("*** ELIMINAR ANIMALES ***")
                self.zoologico.mostrar_animales()
                id_eliminar = input("Ingresa el ID del animal a eliminar: ")
                self.zoologico.eliminar_animal(id_eliminar=id_eliminar)

            elif opcion == "14":
                id= None
                
                print("\nSeleccionaste eliminar empleado\n")

                if self.zoologico.comprobrar_existencia_empleados() == True:

                    print("Lista de empleados registrados: \n")
                    self.zoologico.mostrar_administracion()
                    self.zoologico.mostrar_mantenimiento()
                    self.zoologico.mostrar_veterinarios()
                    self.zoologico.mostrar_guia()

                    while id==None:
                        id=input("Ingrese el ID del empleado a eliminar: ")
                        id=self.zoologico.validar_id_empleado(id)
                else:
                    continue
                
                self.zoologico.eliminar_empleado(id_empleado=id)

            elif opcion == "15":
                
                print("\nSelecionaste la opción de eliminar visitante")
                self.zoologico.mostrar_visitantes()
                
                id = input("\nIngrese el ID del visitante a eliminar: ")

                self.zoologico.eliminar_visitante(id=id)
            
            elif opcion == "16":
                print("\nAdios!!!\n")
                break

            else:
                print("\nOpcion no valida, intente de nuevo\n") 

        
