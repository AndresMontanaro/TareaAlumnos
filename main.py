import alumnos, profesores, cursos
 
def menu():
 
    while True:
        print("\n SISTEMA ESCOLAR DE CALIFICACIONES \n")

        print("1. Agregar\consultar alumnos")
        print("2. Agregar\consultar profesores")
        print("3. Agregar\consultar cursos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                subopcion = input("\na) Agregar alumno\nb) Consultar alumnos\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    nombre = input("\nNombre del alumno: ")

                    if list(filter(lambda alum: alum['nombre']==nombre, alumnos.consultar_alumnos())):
                        print("\nEse nombre de alumno ya existe.")
                        continue
                    
                    cedula = input("Cédula del alumno (9 dígitos): ")

                    if len(cedula) != 9 or not cedula.isdigit():
                        print("\nLa cédula debe ser numérica con solo 9 dígitos.")
                        continue
                    
                    if list(filter(lambda alum: alum['cedula']==cedula, alumnos.consultar_alumnos())) \
                        or list(filter(lambda prof: prof['cedula']==cedula, profesores.consultar_profesores())):
                        print("\nEsa cédula ya existe.")
                        continue
                    
                    if len(cursos.consultar_cursos()) == 0:
                        print("\nNo hay cursos. Tendrás que agregar cursos desde la opción de cursos.")
                        break
                    
                    print("\nCURSOS\n")

                    for curso in cursos.consultar_cursos():
                        print(f"{curso['codigo']}: {curso['nombre']}")   
                        
                    codigo_curso = input("\nCurso del alumno (Código): ")

                    if not list(filter(lambda curs: curs['codigo']==codigo_curso, cursos.consultar_cursos())):
                        print(f"\nNo existe el curso con código: {codigo_curso}. Tendrás que agregarlo en la opción de cursos.")
                        break
                    
                    nota = input("\nNota del alumno: ")
                    
                    if not nota.isdigit():
                        print("\nLa nota debe ser totalmente en número entero.")
                        continue
                    
                    print("\nALUMNO AGREGADO")

                    alumnos.agregar_alumno(nombre, cedula, codigo_curso, nota)

                    break

                elif subopcion == 'b':
                    
                    if len(alumnos.consultar_alumnos()) > 0:
                        print("\nREPORTE DE ALUMNOS\n")
                        print(f"Alumnos encontrados: {len(alumnos.consultar_alumnos())}")

                        promedio = sum(int(alumno['nota']) for alumno in alumnos.consultar_alumnos()) / len(alumnos.consultar_alumnos())

                        print(f"Promedio de las notas: {promedio:.2f}")
                        
                        print(f"Aprobados: {len(list(filter(lambda nota: nota >= 70, 
                                            (int(alumno['nota']) for alumno in alumnos.consultar_alumnos()))))}")
                        
                        print(f"Aplazados: {len(list(filter(lambda nota: 60 <= nota < 70, 
                                            (int(alumno['nota']) for alumno in alumnos.consultar_alumnos()))))}")
                        
                        print(f"Reprobados: {len(list(filter(lambda nota: nota < 60, 
                                            (int(alumno['nota']) for alumno in alumnos.consultar_alumnos()))))}")
                        
                        print(f"Notas superiores al promedio: {len(list(filter(lambda nota: nota > promedio, 
                                                              (int(alumno['nota']) for alumno in alumnos.consultar_alumnos()))))}\n")

                        alumnos_ordenados = sorted(alumnos.consultar_alumnos(), key=lambda alum: alum['nota'], reverse=True)

                        for alumno in alumnos_ordenados:

                            for curso in cursos.consultar_cursos():
                                if curso['codigo'] == alumno['curso']:
                                    curso_alumno = curso['nombre']
                                    break

                            print(f"{str(alumno['cedula']).ljust(8)}: {str(alumno['nombre']).ljust(20)}  "
                                f"{str(curso_alumno).ljust(14)}  {str(alumno['nota']).ljust(11)}  "
                                f"{str("APROBADO" if int(alumno['nota']) >= 70 else "APLAZADO" if 60 <= int(alumno['nota']) < 70 else "REPROBADO").ljust(13)}  "
                                f"{str("SUPERIOR AL PROMEDIO" if int(alumno['nota']) > promedio else "INFERIOR AL PROMEDIO").ljust(16)}") 

                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay alumnos para consultar")

                    break
                
                else:

                    print("\nOPCIÓN INVÁLIDA")
        
        elif opcion == "2":
            while True:
                subopcion = input("\na) Agregar profesor\nb) Consultar profesores\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    cedula = input("\nCédula del profesor (9 dígitos): ")

                    if len(cedula) != 9 or not cedula.isdigit():
                        print("\nLa cédula debe ser numérica con solo 9 dígitos.")
                        continue
                    
                    if list(filter(lambda alum: alum['cedula']==cedula, alumnos.consultar_alumnos())) \
                        or list(filter(lambda prof: prof['cedula']==cedula, profesores.consultar_profesores())):
                        print("\nEsa cédula ya existe.")
                        continue

                    nombre = input("Nombre del profesor: ")

                    if list(filter(lambda prof: prof['nombre']==nombre, profesores.consultar_profesores())):
                        print("\nEse nombre de profesor ya existe.")
                        continue
                    
                    if len(cursos.consultar_cursos()) == 0:
                        print("\nNo hay cursos. Tendrás que agregar cursos desde la opción de cursos.")
                        break
                    
                    print("\nCURSOS\n")

                    for curso in cursos.consultar_cursos():
                        print(f"{curso['codigo']}: {curso['nombre']}")  

                    codigo_curso = input("\nCurso del profesor (Código): ")

                    if not list(filter(lambda curs: curs['codigo']==codigo_curso, cursos.consultar_cursos())):
                        print(f"\nNo existe el curso con código: {codigo_curso}. Tendrás que agregarlo en la opción de cursos.")
                        break
                    
                    print("\nPROFESOR AGREGADO")

                    profesores.agregar_profesor(cedula, nombre, codigo_curso)

                    break

                elif subopcion == 'b':

                    if len(profesores.consultar_profesores()) > 0:

                        print("\nPROFESORES\n")
                        print(f"Profesores encontrados: {len(profesores.consultar_profesores())}\n")

                        for profesor in profesores.consultar_profesores():

                            for curso in cursos.consultar_cursos():
                                if curso['codigo'] == profesor['curso']:
                                    curso_profesor = curso['nombre']
                                    break
                            
                            print(f"{str(profesor['cedula']).ljust(8)}:  {str(profesor['nombre']).ljust(12)}  "
                                  f"{str(curso_profesor).ljust(16)}")

                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay profesores para consultar")

                    break
                
                else:

                    print("\nOPCIÓN INVÁLIDA")

        elif opcion == "3":
            while True:
                subopcion = input("\na) Agregar curso\nb) Consultar cursos\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    codigo_curso = input("\nCódigo del curso: ")

                    if not codigo_curso.isdigit():
                        print("\nEl código debe ser totalmente numérico")
                        continue    
                    
                    if list(filter(lambda curs: curs['codigo']==codigo_curso, cursos.consultar_cursos())):
                        print(f"\nEl código del curso ya existe.")
                        continue

                    nombre = input("Nombre del curso: ")

                    if list(filter(lambda curs: curs['nombre']==nombre, cursos.consultar_cursos())):
                        print("\nEse nombre de curso ya existe.")
                        continue
                    
                    print("\nCURSO AGREGADO")

                    cursos.agregar_curso(codigo_curso, nombre)

                    break

                elif subopcion == 'b':
                    
                    if len(cursos.consultar_cursos()) > 0:
                        
                        print("\nCURSOS\n")
                        print(f"Cursos encontrados: {len(cursos.consultar_cursos())}\n")

                        for curso in cursos.consultar_cursos():
                            
                            print(f"{curso['codigo']}:\t{curso['nombre']}\t"
                                  f"Llevado por: {", ".join([profesor['nombre'] for profesor in profesores.consultar_profesores() 
                                                             if profesor['curso'] == curso['codigo']])}")
                            
                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay cursos para consultar")

                    break
                
                else:

                    print("\nOPCIÓN INVÁLIDA")

        elif opcion == "4":

            print("\nSISTEMA FINALIZADO")
            break
        
        else:

            print("\nOPCIÓN INVÁLIDA")

if __name__=='__main__':
    menu()