from usuarios import Estudiante
from cursos import Curso
from evaluaciones import Evaluacion
from reportes import reporte_promedios_bajos
from almacenamiento import guardar_datos, cargar_datos

curso_python = Curso("Python Básico")
e1 = Estudiante("Maria", 1)
e2 = Estudiante("Carlos", 2)

curso_python.inscribir_estudiante(e1)
curso_python.inscribir_estudiante(e2)

eval1 = Evaluacion("Examen Parcial", "Escrito")
curso_python.evaluaciones.append(eval1)

eval1.registrar_calificacion(e1, 50)
eval1.registrar_calificacion(e2, 90)

reporte_promedios_bajos(curso_python, limite=60)

guardar_datos(curso_python, "curso_python.pkl")

curso_cargado = cargar_datos("curso_python.pkl")
print("Curso cargado:", curso_cargado.nombre)

