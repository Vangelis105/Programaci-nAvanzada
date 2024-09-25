from escuela.escuela import Escuela
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
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros") 
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro") 
    print("12. Eliminar materia") 
    print("13. Salir")

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
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante=estudiante)

    if opcion == "2":
        print("\n+++ Registrar maestro +++")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano_nacimiento = input("Ingresa su año de nacimiento: ")
        rfc = input("Ingresa el RFC: ")
        sueldo = float(input("Ingresa el sueldo por hora: "))
        numero_control = escuela.generar_numeroControl_M(ano_nacimiento, nombre, rfc)
        print("Numero de control: ",numero_control)
        maestro = Maestro(nombre=nombre, apellido=apellido, ano_nacimiento=ano_nacimiento, rfc=rfc, sueldo=sueldo, numero_control=numero_control)
        escuela.registrar_maestro(maestro=maestro)

    if opcion == "3":
        print("\n+++ Registrar materia +++")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ")
        creditos = int(input("Ingresa la cantidad de creditos de la materia: "))
        semestre = int(input("Ingresa el semestre de la materia: "))
        id = escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print("ID: ",id)
        materia = Materia(nombre=nombre, descripcion=descripcion, creditos=creditos, semestre=semestre, id=id)
        escuela.registrar_materia(materia=materia)

    if opcion == "4":
        pass

    if opcion == "5":
        pass

    if opcion == "6":
        escuela.listar_estudiantes()


    if opcion == "7":
        escuela.listar_maestros()

    if opcion == "8":
        escuela.listar_materias()

    if opcion == "9":
        pass

    if opcion == "10":
        print("+++ ELIMINAR ESTUDIANTE +++")
        numero_control = input("Ingresa el número de control del estudiante a elimianr: ")
        escuela.eliminar_estudiante(numero_control)

    if opcion == "11":
        print("+++ ELIMINAR MAESTRO +++")
        numero_control = input("Ingresa el número de control del maestro a elimianr: ")
        escuela.eliminar_maestro(numero_control)

    if opcion == "12":
        print("+++ ELIMINAR MATERIA +++")
        id = input("Ingresa el ID de la materia a elimianr: ")
        escuela.eliminar_materia(id)

    if opcion == "13":
        print("Adios =)")
        break
    