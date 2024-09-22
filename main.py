from tec.tec import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime

escuela = Escuela()

while True:
    print("\n** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")

    opcion = input("Ingresa una opcion para continuar: ")


    if opcion == "1":
        print("\n+++ Registrar estudiante +++")
        numero_control = escuela.generar_numeroControl_E()
        print("Numero de control: ",numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la CURP del estudiante: ")
        print("Ingresa su fecha de nacimiento: ")
        año = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Dia: "))
        fecha_nacimiento = datetime(año, mes, dia)
        escuela.registrar_estudiante(Estudiante)

    if opcion == "2":
        print("\n+++ Registrar maestro +++")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano_nacimiento = int(input("Ingresa su año de nacimiento: "))
        rfc = input("Ingresa el RFC: ")
        sueldo = float(input("Ingresa el sueldo por hora: "))
        numero_control = escuela.generar_numeroControl_M(ano_nacimiento, nombre, rfc)
        print("Numero de control: ",numero_control)
        escuela.registrar_maestro(Maestro)

    if opcion == "3":
        print("\n+++ Registrar materia +++")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ")
        creditos = int(input("Ingresa la cantidad de creditos de la materia: "))
        semestre = int(input("Ingresa el semestre de la materia: "))
        id = escuela.generar_id_materia(nombre, semestre, creditos)
        print("ID: ",id)
        escuela.registrar_materia(Materia)

    if opcion == "4":
        pass

    if opcion == "5":
        pass

    if opcion == "6":
        print("Adios =)")
        break
    