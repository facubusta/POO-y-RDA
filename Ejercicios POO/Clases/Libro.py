class Libro:

    def __init__(self, titulo: str, autor: str, año_publicacion: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self) ->None:
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")
        
