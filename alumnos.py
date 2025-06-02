alumnos = []

def agregar_alumno(nombre, cedula, curso, nota):
    alumno = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso,
        'nota': nota
    }

    alumnos.append(alumno)

def consultar_alumnos():
    return alumnos