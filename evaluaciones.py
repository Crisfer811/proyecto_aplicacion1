class Evaluacion:
    def __init__(self, titulo, tipo, ponderacion):
        self.titulo = titulo
        self.tipo = tipo
        self.ponderacion = ponderacion
        self.notas = {}

    def asignar_nota(self, estudiante, nota):
        if estudiante not in self.notas:
            self.notas[estudiante] = nota
            estudiante.notas[self] = nota
        else:
            raise Exception("Nota ya registrada")

    def obtener_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
