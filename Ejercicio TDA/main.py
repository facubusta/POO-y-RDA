from paquetes.preceptores import *
from paquetes.alumnos import *

alumnos = []
cursos = {}
ejecutar = True

while ejecutar:
    
    print("Menu de Opciones:")
    print("1. Cargar Alumnos")
    print("2. Cargar Cursos")
    print("3. Generar Set de Preceptores por Año")
    print("4. Obtener Promedio de Edad de un Curso")
    print("5. Buscar Preceptores Repetidos en dos Años")
    print("6. Buscar Preceptores Solo en un Año")
    print("7. Mostrar Alumnos Más Jóven y Más Grande")
    print("0. Salir")

    opcion = input("Ingresa la opción que deseas realizar: ")

    match opcion:
        case "1":
            cantidad = int(input("¿Cuántos alumnos deseas agregar? "))
            for _ in range(cantidad):
                nombre = input("Ingresa el nombre del alumno: ")
                apellido = input("Ingresa el apellido del alumno: ")
                edad = int(input("Ingresa la edad del alumno: "))
                curso_input = input("Ingresa el curso del alumno (ej. '1 117'): ")  
                curso = tuple(curso_input.split())
                alumno = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "edad": edad,
                    "curso": curso  
                }
                alumnos.append(alumno)
                print(f"Alumno {nombre} {apellido} agregado correctamente.")
                print(alumnos)
            
        case "2":
            cantidad = int(input("¿Cuántos cursos deseas agregar? "))
            for _ in range(cantidad):
                año = input("Ingresa el año del curso: ")
                division = input("Ingresa la división del curso: ")
                preceptor = input("Ingresa el nombre del preceptor: ")
                cantidad_alumnos = int(input("Ingresa la cantidad de alumnos: "))
                cursos[(año, division)] = {
                    "cantidad_alumnos": cantidad_alumnos,
                    "preceptor": preceptor }
                print(f"Curso {año} {division} agregado correctamente.")
            for clave, detalles in cursos.items():
                print(f"Curso: {clave[0]} {clave[1]}")
                print(f"Preceptor: {detalles['preceptor']}, Cantidad de alumnos: {detalles['cantidad_alumnos']}")
        
        case "3":
            preceptores = set() 
            for curso in cursos:
                preceptores.add(curso['preceptor'])
            print(f"Set de preceptores: {preceptores}")

        case "4":
            curso_input = input("Ingresa el curso para el cual deseas calcular el promedio de edad: ") 
            curso_convertido = tuple(curso_input.split())
            edades = []
            for alumno in alumnos:  
                if alumno['curso'] == curso_convertido:  
                    edades.append(alumno['edad'])  
            print(f"Edades de los alumnos en el curso '{curso_input}': {edades}")  
            if edades:  
                promedio = sum(edades) / len(edades) 
                print(f"Promedio de edad en el curso '{curso_input}' es de: {promedio:.2f}") 
            else:
                print(f"No hay alumnos en el curso '{curso_input}'. No se puede calcular el promedio.")
                
        case "5":
            año1 = input("Ingresa el primer año: ")
            año2 = input("Ingresa el segundo año: ")
            preceptores_repetidos = buscar_preceptores_repetidos(cursos, año1, año2)
            if preceptores_repetidos:
                print(f"Preceptores repetidos en los años {año1} y {año2}: {', '.join(preceptores_repetidos)}")
            else:
                print(f"No hay preceptores repetidos en los años {año1} y {año2}.")
                
        case "6":
            año = input("Ingresa el año para buscar preceptores: ")
            preceptores = buscar_preceptores_año(cursos, año)
            if preceptores:
                print(f"Preceptores solo en el año {año}: {', '.join(preceptores)}")
            else:
                print(f"No hay preceptores que solo estén en el año {año}.")
        
        case "7":
            mostrar_alumnos_joven_y_grande(alumnos)
                
        case "0":
            print("Se salió del ejercicio")
            ejecutar = False