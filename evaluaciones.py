class Evaluacion:
  def __init__(self, nombre, tipo, ponderacion = 1.0):
    self.nombre = nombre 
    self.tipo = tipo
    self.ponderacion = ponderacion 
    self.calificacion = {}

  def registrar_calificacion(self, estudiante, nota, comentarios):
    try:
      if 0 <= nota <=100:
        self.calificacion[estudiante.id_usuario] = {
          "nota": nota,
          "comentario": comentarios
        }else:
        raise ValueError
