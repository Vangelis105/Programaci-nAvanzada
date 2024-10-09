from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo
from datetime import datetime
from usuario.utils.roles import Rol

class Menu:
    escuela: Escuela = Escuela()


    def login(self):
        intentos = 0
        while intentos < 5:

            print("\n\t*** BIENVENIDO ***")
            print("Inicia sesión para continuar")
            numero_control = input("Ingresa tu numero de control: ")
            contraseña_usuario = input("Ingresa tu contraseña: ")
            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contraseña=contraseña_usuario)
            if usuario is None:
                intentos = self.mostrar_intentos(intentos=intentos)
            else: 
                if usuario.rol == Rol.ESTUDIANTE:
                    print("ERES ESTUDIANTE")
                    self.mostrar_menu_Estudiante(usuario)
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    print("ERES MAESTRO")
                    self.mostrar_menu_Maestro(usuario)
                    intentos = 0

                else:
                    print("ERES COORDINADOR")
                    self.mostrar_menu()
                    intentos = 0

    def mostrar_intentos(self, intentos):
        print("Nombre o contraseña incorrecta. Intenta de nuevo")
        return intentos + 1   

    def mostrar_menu_Estudiante(self, usuario):
        opcion = 0
        while opcion != 4:
            print("\n\t *** Menu de estudiante ***")
            print("1. Ver horario")
            print("2. Mostrar materias")
            print("3. Ver mi informacion")
            print("4. Salir")
            
            opcion = int(input("Ingresa una opcion"))
            if opcion == 3:
                print(usuario.mostrar_info_estudiante())
            elif opcion == 4:
                break

    def mostrar_menu_Maestro(self, usuario):
        print("\n\t *** Menu de maestro ***")
        opcion = 0
        while opcion != 4:
            print("\n\t *** Menu de maestro ***")
            print("1. Ver horario")
            print("2. Mostrar materias")
            print("3. Ver mi informacion")
            print("4. Salir")
            
            opcion = int(input("Ingresa una opcion"))
            if opcion == 3:
                print(usuario.mostrar_info_maestro())
        
            elif opcion == 4:
                break    

    def mostrar_menu(self):

        while True:
            print("\n\t** MINDBOX **")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo")
            print("5. Registrar horario")
            print("6. Mostrar estudiantes")
            print("7. Mostrar maestros") 
            print("8. Mostrar materias")
            print("9. Mostrar grupos")
            print("10. Eliminar estudiante")
            print("11. Eliminar maestro") 
            print("12. Eliminar materia") 
            print("13. Registrar carrera")
            print("14. Registrar un semestre")
            print("15. Mostrar carrera")
            print("16. Mostrar semestre")
            print("17. Salir")

            opcion = input("Ingresa una opcion para continuar: ")
            


            if opcion == "1":
                print("\n\t+++ Registrar estudiante +++")
                numero_control = self.escuela.generar_numeroControl_E()
                print("Numero de control: ",numero_control)
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la CURP del estudiante: ")
                print("Ingresa su fecha de nacimiento: ")
                año = int(input("Año: "))
                mes = int(input("Mes: "))
                dia = int(input("Dia: "))
                fecha_nacimiento = datetime(año, mes, dia)
                contraseña = input("Ingresa tu contraseña: ")
                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contraseña=contraseña)
                self.escuela.registrar_estudiante(estudiante=estudiante)

            if opcion == "2":
                print("\n\t+++ Registrar maestro +++")
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                ano_nacimiento = input("Ingresa su año de nacimiento: ")
                rfc = input("Ingresa el RFC: ")
                sueldo = float(input("Ingresa el sueldo por hora: "))
                numero_control = self.escuela.generar_numeroControl_M(ano_nacimiento, nombre, rfc)
                print("Numero de control: ",numero_control)
                contraseña = input("Ingresa tu contraseña: ")
                maestro = Maestro(nombre=nombre, apellido=apellido, ano_nacimiento=ano_nacimiento, rfc=rfc, sueldo=sueldo, numero_control=numero_control, contraseña=contraseña)
                self.escuela.registrar_maestro(maestro=maestro)

            if opcion == "3":
                print("\n\t+++ Registrar materia +++")
                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripcion de la materia: ")
                creditos = int(input("Ingresa la cantidad de creditos de la materia: "))
                semestre = int(input("Ingresa el semestre de la materia: "))
                id = self.escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
                print("ID: ",id)
                materia = Materia(nombre=nombre, descripcion=descripcion, creditos=creditos, semestre=semestre, id=id)
                self.escuela.registrar_materia(materia=materia)

            if opcion == "4":
                print("\n\t+++ REGISTRAR GRUPO +++")
                tipo = input("Ingresa el tipo de grupo (A/B): ")
                id_semestre = input("Ingresa el ID del semestre al que pertence el grupo: ")
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)
                
                
            if opcion == "5":
                pass

            if opcion == "6":
                self.escuela.listar_estudiantes()

            if opcion == "7":
                self.escuela.listar_maestros()

            if opcion == "8":
                self.escuela.listar_materias()

            if opcion == "9":
                self.escuela.listar_grupos()

            if opcion == "10":
                print("\n\t+++ ELIMINAR ESTUDIANTE +++")
                numero_control = input("Ingresa el número de control del estudiante a elimianr: ")
                self.escuela.eliminar_estudiante(numero_control)

            if opcion == "11":
                print("\n\t+++ ELIMINAR MAESTRO +++")
                numero_control = input("Ingresa el número de control del maestro a elimianr: ")
                self.escuela.eliminar_maestro(numero_control)

            if opcion == "12":
                print("\n\t+++ ELIMINAR MATERIA +++")
                id = input("Ingresa el ID de la materia a elimianr: ")
                self.escuela.eliminar_materia(id)
            
            if opcion == "13":
                print("\n\t+++ REGISTRAR CARRERA +++")
                nombre = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera)
                
            if opcion == "14":
                print("\n\t+++ REGISTRAR SEMESTRE")
                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")
                
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)
                
            if opcion == "15":
                self.escuela.listar_carreras()
                
            if opcion == "16":
                self.escuela.listar_semestres()
                
            if opcion == "17":
                print("Adios =)")
                break