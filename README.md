# Manual de Usuario – Plataforma de Gestión de Cursos Online
 1.  INTRODUCCION
Este sistema permite gestionar cursos online, inscribir a estudiantes, crear evaluaciones y registrar calificaciones. El programa como tal esta diseñado en Python usando Programacion Orientada a Objetos (POO)
 2.  ALGUNOS REQUISITOS
- Python (Obviamente)
- Consola, puede ser VS Code o PyCharm
  
  3. INICIAR EL PROGRAMA
- Abrir el archivo (Plataforma.py) en Python
- Ejecutar el programa
    
  4. ROLES DEL USUARIO
* Instructor
  - Puede crear cursos
  - Puede crear avaluaciones
  - Puede asignar notas
    + EJEMPLO
       profe = Instructor("Carlos Batres", "C01", "carbat@uni.edu.gt")
       curso1 = profe.crear_curso("C101", "Estructura de Datos")
       examen1 = profe.crear_evaluacion(curso1, "Parcial 1", "Examen Parcial")
 * Estudiante
   - Puede inscribirse a un curso
   - puede consultar sus notas
     + EJEMPLO
       est1 = Estudiante("Danna Espino ", "EST001", "danne@est.edu")
       est1.inscribir(curso1)

  5. FUNCIONES PRINCIPALES
    1. Crear Curso
      - Solo el instructor puede hacerlo
      - Requiere: Codigo y Nombre del curso
    2. Inscribir Estudiante
      - Relaciona un estudiante con un curso
      - Si ya esta inscrito, el sistema mostrara un error
    3. Crear Evaluacion
      - El instructor define titulo y tipo (Examen o tarea)
      - La evaluacion se almacena con el curso correspondiente 
    4. Registrar Calificacion
      - Se asigna una nota a un estudiante en una evaluacion
      - Si ya existe nota, se mostrara un error
    5. Reporte De Promedios Bajos
      - El sistema calcula el promedio de cada estudiante
      - Muestra aquellos que estan por debajo de un limite definido
     
  6. EJEMPLO DE FLUJO
    # Crear Maestro y curso
     profe = Instructor("Carlos Batres", "C01", "carbat@uni.edu.gt")
     curso1 = profe.crear_curso("C101", "Estructura de Datos")
     
     # Crear estudiantes e inscribirlos
     est1 = Estudiante("Danna Espino ", "EST001", "danne@est.edu")
     est2 = Estudiante("Hanna Espino", "EST002", "hanna@est.edu")
     est1.inscribir(curso1)
     est2.inscribir(curso1)
     
     # Crear evaluación y asignar notas
     examen1 = profe.crear_evaluacion(curso1, "Parcial 1", "Examen Parcial")
     examen1.asignar_nota(est1, 60)
     examen1.asignar_nota(est2, 45)
     
     # Generar reporte de estudiantes con promedio menor a 50
     reporte_promedios_bajos(curso1, 50)

     Hanna Espino tiene promedio bajo: 40.00
      
  7. MANEJO DE ERRORES
     Inscripción duplicada → “El estudiante ya está inscrito en este curso”.
     Nota duplicada → “Ya existe una nota para este estudiante”.
     Instructor no imparte curso → Error al crear evaluación.

   
