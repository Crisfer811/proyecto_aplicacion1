class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_estudiante})"
