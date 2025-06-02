cursos = []

def agregar_curso(codigo, nombre):
    curso = {
        'codigo':codigo,
        'nombre':nombre,
    }

    cursos.append(curso)

def consultar_cursos():
    return cursos