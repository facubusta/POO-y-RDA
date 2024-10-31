def mostrar_alumnos_joven_y_grande(alumnos: list) ->None:
    '''
    Muestra por pantalla el nombre y apellido 
    del alumno mas joven y mas grande
    '''
    alumno_mas_joven = alumnos[0]
    for alumno in alumnos:
        if alumno['edad'] < alumno_mas_joven['edad']:
            alumno_mas_joven = alumno

    alumno_mas_grande = alumnos[0]
    for alumno in alumnos:
        if alumno['edad'] > alumno_mas_grande['edad']:
            alumno_mas_grande = alumno

    print(f"El alumno más joven es: {alumno_mas_joven['nombre']} {alumno_mas_joven['apellido']} con {alumno_mas_joven['edad']} años.")
    print(f"El alumno más grande es: {alumno_mas_grande['nombre']} {alumno_mas_grande['apellido']} con {alumno_mas_grande['edad']} años.")