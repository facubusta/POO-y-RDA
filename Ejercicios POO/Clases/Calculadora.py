class Calculadora:

    def __init__(self, parametro_1: float, parametro_2: float) -> None:
        self.parametro_1 = parametro_1
        self.parametro_2 = parametro_2
    
    def calcular_suma(self) ->float:
        return self.parametro_1 + self.parametro_2
    
    def calcular_resta(self) ->float:
        return self.parametro_1 - self.parametro_2
    
    def calcular_multiplicacion(self) ->float:
        return self.parametro_1 * self.parametro_2
   
    def calcular_division(self) ->float:
        return self.parametro_1 / self.parametro_2
        