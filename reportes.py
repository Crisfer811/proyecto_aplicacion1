def reporte_promedios_bajos(curso, limite):
    resultado = []
    for estudiante in curso.estudiantes:
        total = 0
        for evaluacion in curso.evaluaciones:
            if estudiante in evaluacion.notas:
                nota = evaluacion.notas[estudiante]
                total += nota * (evaluacion.ponderacion / 100)
        if total > 0 and total < limite:
            resultado.append((estudiante.nombre, f"{total:.2f}/100"))
    return resultado
