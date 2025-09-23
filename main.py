import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from usuarios import Instructor, Estudiante
from reportes import reporte_promedios_bajos

instructores = []
estudiantes = []
cursos = []

def pedir_campo(titulo, mensaje):
    valor = None
    while not valor:
        valor = simpledialog.askstring(titulo, mensaje)
        if not valor:
            messagebox.showwarning("Hey tú", f"Debes ingresar {mensaje.lower()}.")
    return valor

#===============Funciones de la interfaz gráfica=============
def crear_instructor():
    nombre = pedir_campo("Instructor", "Nombre")
    carnet = pedir_campo("Instructor", "Carnet")
    email = pedir_campo("Instructor", "Email")
    inst = Instructor(nombre, carnet, email)
    instructores.append(inst)
    actualizar()
    messagebox.showinfo("Felicidades, Vamossss!!", f"Instructor {nombre} creado.")

def crear_estudiante():
    nombre = pedir_campo("Estudiante", "Nombre")
    carnet = pedir_campo("Estudiante", "Carnet")
    email = pedir_campo("Estudiante", "Email")
    est = Estudiante(nombre, carnet, email)
    estudiantes.append(est)
    actualizar()
    messagebox.showinfo("Felicidades, Vamossss!!", f"Estudiante {nombre} creado.")

def crear_curso():
    if not instructores:
        messagebox.showwarning("Ey espera", "Debe crear un instructor primero.")
        return
    if instructor_cb.current() < 0:
        messagebox.showwarning("Ey porfa", "Seleccione un instructor.")
        return
    inst = instructores[instructor_cb.current()]
    codigo = pedir_campo("Curso", "Código del curso")
    nombre = pedir_campo("Curso", "Nombre del curso")
    curso = inst.crear_curso(codigo, nombre)
    cursos.append(curso)
    actualizar()
    messagebox.showinfo("Felicidades", f"Curso {nombre} creado por {inst.nombre}")

def inscribir_estudiante():
    if not estudiantes or not cursos:
        messagebox.showwarning("Ey espera", "Debe haber estudiantes y cursos.")
        return
    if student_cb.current() < 0 or course_cb.current() < 0:
        messagebox.showwarning("Ey que haces", "Selecciona un estudiante y un curso.")
        return
    est = estudiantes[student_cb.current()]
    curso = cursos[course_cb.current()]
    try:
        est.inscribir(curso)
        messagebox.showinfo("Éxito", f"{est.nombre} inscrito en {curso.nombre}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_evaluacion():
    if course_cb.current() < 0:
        messagebox.showwarning("Cuidado", "Seleccione un curso.")
        return
    curso = cursos[course_cb.current()]
    titulo = pedir_campo("Evaluación", "Título de la evaluación")
    tipo = pedir_campo("Evaluación", "Tipo (examen/tarea)")

    ponderacion = None
    while ponderacion is None:
        try:
            p = simpledialog.askstring("Evaluación", "Ponderación (%)")
            if not p:
                messagebox.showwarning("precaución", "Debe ingresar una ponderación.")
                continue
            ponderacion = float(p)
            if ponderacion <= 0 or ponderacion > 100:
                messagebox.showwarning("Pues que te digo", "La ponderación debe estar entre 1 y 100.")
                ponderacion = None
        except ValueError:
            messagebox.showwarning("Atención", "Ingrese un número válido.")

    evaluacion = curso.instructor.crear_evaluacion(curso, titulo, tipo, ponderacion)
    messagebox.showinfo("Éxito", f"Evaluación {titulo} creada con {ponderacion}% en {curso.nombre}")

def asignar_nota():
    if course_cb.current() < 0:
        messagebox.showwarning("Es enserio :(", "Seleccione un curso.")
        return
    curso = cursos[course_cb.current()]
    if not curso.evaluaciones:
        messagebox.showwarning("Ja", "Ese curso no tiene evaluaciones.")
        return
    if student_cb.current() < 0:
        messagebox.showwarning("Es por orden", "Seleccione un estudiante.")
        return
    estudiante = estudiantes[student_cb.current()]
    evaluacion = curso.evaluaciones[0]  # simple: primera evaluación

    nota = None
    while nota is None:
        try:
            n = simpledialog.askstring("Nota", f"Ingrese nota (0-100) para {estudiante.nombre}:")
            if not n:
                messagebox.showwarning("ey ey ey", "Debe ingresar una nota.")
                continue
            nota = float(n)
            if nota < 0 or nota > 100:
                messagebox.showwarning("Por segunda vez", "La nota debe estar entre 0 y 100.")
                nota = None
        except ValueError:
            messagebox.showwarning("Ja", "Ingrese un número válido.")

    try:
        evaluacion.asignar_nota(estudiante, nota)
        messagebox.showinfo("Éxito", f"Nota {nota} asignada a {estudiante.nombre}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reporte():
    if course_cb.current() < 0:
        messagebox.showwarning("Atención", "Seleccione un curso.")
        return
    curso = cursos[course_cb.current()]
    reporte = reporte_promedios_bajos(curso, 50)
    if not reporte:
        messagebox.showinfo("Reporte de promedios bajos", "No hay estudiantes con promedio bajo.")
    else:
        texto = "\n".join([f"{n}: {p}" for n, p in reporte])
        messagebox.showinfo("Reporte", texto)

def ver_usuarios():
    if not instructores and not estudiantes:
        messagebox.showinfo("Usuarios", "No hay usuarios creados todavía.")
        return
    
    texto = "  INSTRUCTORES:\n"
    if instructores:
        for i in instructores:
            texto += f"- {i.nombre} ({i.carnet}) - {i.email}\n"
    else:
        texto += "Ninguno\n"
    
    texto += "\n  ESTUDIANTES:\n"
    if estudiantes:
        for e in estudiantes:
            texto += f"- {e.nombre} ({e.carnet}) - {e.email}\n"
    else:
        texto += "Ninguno\n"

    messagebox.showinfo("Usuarios creados", texto)

def ver_cursos():
    if not cursos:
        messagebox.showinfo("Cursos", "No hay cursos creados todavía.")
        return
    
    texto = "  CURSOS:\n"
    for c in cursos:
        texto += f"\n{c.codigo} - {c.nombre} (Instructor: {c.instructor.nombre})\n"
        
        if c.estudiantes:
            texto += "      Estudiantes:\n"
            for e in c.estudiantes:
                texto += f"        - {e.nombre} ({e.carnet})\n"
        else:
            texto += "   * Sin estudiantes inscritos\n"
        
        if c.evaluaciones:
            texto += "     Evaluaciones:\n"
            for ev in c.evaluaciones:
                texto += f"      - {ev.titulo} ({ev.tipo}) - {ev.ponderacion}%\n"
                
                if ev.notas:
                    for est, nota in ev.notas.items():
                        texto += f"          > {est.nombre}: {nota}\n"
                else:
                    texto += "          * Sin notas asignadas\n"
        else:
            texto += "   * Sin evaluaciones creadas\n"

    messagebox.showinfo("Perfecto Cursos creados", texto)

def actualizar():
    instructor_cb["values"] = [f"{i.nombre}" for i in instructores]
    student_cb["values"] = [f"{s.nombre}" for s in estudiantes]
    course_cb["values"] = [f"{c.nombre}" for c in cursos]

#=============Inicio de la interfaz gráfica=============
root = tk.Tk()
root.title("Plataforma de Cursos")
root.geometry("450x650")

tk.Button(root, text="Crear Instructor", command=crear_instructor).pack(pady=5)
tk.Button(root, text="Crear Estudiante", command=crear_estudiante).pack(pady=5)
tk.Button(root, text="Ver Usuarios", command=ver_usuarios).pack(pady=5)

tk.Label(root, text="Instructor:").pack()
instructor_cb = ttk.Combobox(root, state="readonly")
instructor_cb.pack(fill="x", padx=10)
tk.Button(root, text="Crear Curso", command=crear_curso).pack(pady=5)

tk.Label(root, text="Estudiante:").pack()
student_cb = ttk.Combobox(root, state="readonly")
student_cb.pack(fill="x", padx=10)
tk.Label(root, text="Curso:").pack()
course_cb = ttk.Combobox(root, state="readonly")
course_cb.pack(fill="x", padx=10)
tk.Button(root, text="Inscribir Estudiante", command=inscribir_estudiante).pack(pady=5)

tk.Button(root, text="Crear Evaluación", command=crear_evaluacion).pack(pady=5)
tk.Button(root, text="Asignar Nota", command=asignar_nota).pack(pady=5)

tk.Button(root, text="Reporte Promedios Bajos", command=reporte).pack(pady=5)

tk.Button(root, text="Ver Cursos, Evaluaciones y Notas", command=ver_cursos).pack(pady=5)

tk.Button(root, text="Cerrar", command=root.destroy, bg="red", fg="white").pack(pady=10)

root.mainloop()
