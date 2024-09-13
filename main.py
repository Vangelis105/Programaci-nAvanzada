from curso import Curso
from estudiante import Estudiante


curso_uno = Curso("Programacion Avanzada",1,"Eder Rivera Cisneros")
curso_dos = Curso("Calculo Integral",2,"Norma Liliana")
curso_tres = Curso("Electromagnetismo",3,"Mona Arjang")

estudiante_1 = Estudiante("Kevin Ivan Garcia Hernandez", 19,22121082)
estudiante_2 = Estudiante("Miguel Angel Mendez Lemus",20,22121081)


estudiante_1.agregar_curso(curso_uno)
estudiante_1.agregar_curso(curso_tres)

estudiante_2.agregar_curso(curso_uno)
estudiante_2.agregar_curso(curso_dos)


curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_1.mostrar_informacion()
estudiante_2.mostrar_informacion()