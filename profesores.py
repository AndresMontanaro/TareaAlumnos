profesores = []

def agregar_profesor(cedula, nombre, curso):
    profesor = {
        'cedula':cedula,
        'nombre':nombre,
        'curso':curso
    }

    profesores.append(profesor)

def consultar_profesores():
    return profesores