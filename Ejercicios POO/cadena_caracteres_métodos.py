#Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una cadena.
def invertir_orden_caracteres(cadena: str) ->str:
    '''
    Invierte el orden de los caracteres de una cadena
    '''
    invertida = "".join(reversed(cadena))
    
    return invertida

cadena_1 = invertir_orden_caracteres("cadena")
print(cadena_1)
print("-------------------------------------------------------------------")

#Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
def contar_palabras(cadena: str) -> int:
    '''
    Cuenta cuantas palabras tiene un string
    '''
    palabras = cadena.split()

    return len(palabras)

texto_1 = "Esto es programación"
print(contar_palabras(texto_1))
print("-------------------------------------------------------------------")

#Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
#en una cadena.
def reemplazar_palabra(cadena: str, palabra_vieja: str, palabra_nueva: str) ->str:
    '''
    Reemplaza una palabra por otra en un string
    '''
    return cadena.replace(palabra_vieja, palabra_nueva)

cadena = "Esto es programacion."
palabra_vieja = "Esto"
palabra_nueva = "No"

cadena_nueva = reemplazar_palabra(cadena, palabra_vieja, palabra_nueva)
print(cadena_nueva)
print("-------------------------------------------------------------------")

#Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
#cadena y muestre:
#ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
def mostrar_peliculas(lista_peliculas: list) ->None:
    '''
    Convierte los elementos de una lista en una
    cadena y muestra la recomendació
    '''
    for peliculas in lista_peliculas:
        if len(peliculas) > 1:
            cadena = ', '.join(f'"{peli}"' for peli in peliculas[:-1])
            cadena += f' y "{peliculas[-1]}"'
        else:
            cadena = f'"{peliculas[0]}"'

        print(f'Se recomienda ver {cadena}.')

lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"],
    ["Blade Runner", "El Rey León", "Volver al Futuro"],
    ["La La Land", "El Gran Lebowski", "Blade Runner"],
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"],
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby", "Hola", "Chau"]
    ]
mostrar_peliculas(lista_peli)
print("-------------------------------------------------------------------")

#Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena
def capitalizar_palabras(cadena: str) ->str:
    '''
    Pone en mayusculas la primera letra de 
    todas las palabras de un string
    '''
    return cadena.title()

palabra_capitalizar = "hola soy una palabra"
print(capitalizar_palabras(palabra_capitalizar))
print("-------------------------------------------------------------------")

#Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
def verificar_palindromo(cadena: str) ->str:
    '''
    Verifica sin un string es un palindromo
    '''
    cadena = cadena.replace(" ", "").lower()
    izquierda = 0
    derecha = len(cadena) - 1
    
    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]:
            return False
        izquierda += 1
        derecha -= 1
        
    return True

texto = "Arriba La Birra"
print(verificar_palindromo(texto))
print("-------------------------------------------------------------------")

#Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o
#-1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
#parámetros) o descendente (si recibió -1)
def ordenar_cadena(cadena: str, orden: int = 1) ->str:
    '''
    Devuelve un string ordenado de forma ascendente
    o descendente segun corresponda.
    '''
    cadena = cadena.replace(" ", "")
    if orden == 1:
        cadena_ordenada = sorted(cadena)  
    else:
        cadena_ordenada = sorted(cadena, reverse=True)  
    
    return ''.join(cadena_ordenada)

texto = "hola mundo"
print(ordenar_cadena(texto))      
print(ordenar_cadena(texto, -1))