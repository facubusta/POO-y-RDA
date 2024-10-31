from Clases.Animal import *

class Gato(Animal):
    
    def __init__(self, nombre: str, sonido: str) -> None:
        super().__init__(nombre)
        self.sonido = sonido
    
    def hacer_sonido(self) ->str:
        return self.sonido