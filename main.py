"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("+++ Bienvenido al sistema del hospital +++")

    print("1. Registrar paciente")
    print("2. Registrar medico")
    print("3. Mostrar pacientes")
    print("4. Mostrar medicos")
    print("5. Eliminar pacientes")
    print("6. Eliminar medicos")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")

    opcion_usuario = input("Selecciona la opcion deseada")

    if opcion_usuario == "1":
        print("\n+++ Registrar paciente +++")
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el ano de nacimiento: "))
        peso = float(input("Ingresa el peso: "))
        estatura = float(input("Ingresa la estatura: "))
        direccion = input("Ingresa la direccion: ")

        paciente = Paciente(nombre, ano_nacimiento, peso, estatura, direccion)
        hospital.registrar_paciente(paciente)
        print("\n Paciente registrado correctamente")
        

    elif opcion_usuario == "2":
        print("\n+++ Registrar medico +++")
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el ano de nacimiento: "))
        rfc = input("Ingresa el RFC: ")
        direccion = input("Ingresa la direccion: ")

        medico = Medico(nombre, ano_nacimiento, rfc, direccion)
        hospital.registrar_medico(medico)
        print("\n Medico registrado correctamente")
        

    elif opcion_usuario == "3":
        hospital.mostrar_pacientes()

    elif opcion_usuario == "4":
        hospital.mostrar_medicos()

    elif opcion_usuario == "5":
        hospital.eliminar_paciente()

    elif opcion_usuario == "6":
        hospital.eliminar_medico()

    elif opcion_usuario == "7":
        hospital.mostrar_pacientes_mayores()

    elif opcion_usuario == "8":
        hospital.mostrar_pacientes_menores()

    elif opcion_usuario == "9":
        print("Hasta luego =)")
        break
        


    