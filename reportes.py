def reporte_promedios_bajos(curso, limite):
    for estudiante in curso.estudiantes:
        total = 0
        cantidad = 0
        for evaluacion in curso.evaluaciones:
            if estudiante in evaluacion.notas:
                total += evaluacion.notas[estudiante]
                cantidad += 1
        if cantidad > 0:
            promedio = total / cantidad
            if promedio < limite:
                print(f"⚠{estudiante.nombre} tiene un promedio bajo: {promedio:.2f}")
