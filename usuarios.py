from cursos import Curso

class Usuario:
    def __init__(self, nombre, carnet, email):
        self.nombre = nombre
        self.carnet = carnet
        self.email = email

    def mostrar_info(self):
        return f"{self.nombre} ({self.carnet}) - {self.email}"


class Estudiante(Usuario):
    def __init__(self, nombre, carnet, email):
        super().__init__(nombre, carnet, email)
        self.cursos = []
        self.notas = {}

    def inscribir(self, curso: Curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.inscribir_estudiante(self)
        else:
            raise Exception("El estudiante ya está inscrito")


class Instructor(Usuario):
    def __init__(self, nombre, carnet, email):
        super().__init__(nombre, carnet, email)
        self.cursos = []

    def crear_curso(self, codigo, nombre):
        from cursos import Curso
        curso = Curso(codigo, nombre, self)
        self.cursos.append(curso)
        return curso

    def crear_evaluacion(self, curso, titulo, tipo):
        from evaluaciones import Evaluacion
        if curso in self.cursos:
            evaluacion = Evaluacion(titulo, tipo)
            curso.agregar_evaluacion(evaluacion)
            return evaluacion
        else:
            raise Exception("El instructor no imparte este curso")



