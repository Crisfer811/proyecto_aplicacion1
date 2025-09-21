class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    def inscribir_estudiante(self, estudiante):
       if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
        else:
            raise Exception("Estudiante ya inscrito en este curso")
    
    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)
    
    def listar_estudiantes(self):
        return [est.mostrar_info() for est in self.estudiantes]
    
