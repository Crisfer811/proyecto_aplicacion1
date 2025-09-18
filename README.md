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
  - puede crear avaluaciones
  - puede asignar notas
    + EJEMPLO
       profe = Instructor("Carlos Pérez", "I001", "carlos@uni.edu")
       curso1 = profe.crear_curso("CS101", "Programación Avanzada")
       examen1 = profe.crear_evaluacion(curso1, "Parcial 1", "examen")
 * Estudiante
   - Puede inscribirse a un curso
   - puede consultar sus notas
     + EJEMPLO
       est1 = Estudiante("Ana López", "E001", "ana@uni.edu")
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

      
      
  8. MANEJO DE ERRORES

   
