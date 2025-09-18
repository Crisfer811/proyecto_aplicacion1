class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        self.evaluaciones = []

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            raise Warning("Estudiante ya agregado")
        self.estudiantes.append(estudiante)
        print(f" {estudiante.nombre} inscrito correctamente en {self.nombre}")

