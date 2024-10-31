from Clases.Libro import *
from Clases.Rectangulo import *
from Clases.Calculadora import *
from Clases.Gato import *
from Clases.Perro import *
from Clases.CuentaBancaria import *

libro_1 = Libro("Escrito en las estrellas", "Sidney Sheldon", 1992)
libro_1.mostrar_informacion()

rectangulo_1 = Rectangulo(2, 5)
print(f"El area del rectangulo es de: {rectangulo_1.calcular_area()}")
print(f"El perimetro del rectangulo es de: {rectangulo_1.calcular_perimetro()}")

calculadora_1 = Calculadora(25, 30)
print(f"la suma es de: {calculadora_1.calcular_suma()}")
print(f"la resta es de: {calculadora_1.calcular_resta()}")
print(f"la multiplicación es de: {calculadora_1.calcular_multiplicacion()}")
print(f"la división es de: {calculadora_1.calcular_division()}")

perro_1 = Perro("Pimienta", "gua gua")
print(f"Mi perra {perro_1.nombre} hace {perro_1.hacer_sonido()} ")
gato_1 = Gato("Cayena", "miau")
print(f"Mi gata {gato_1.nombre} hace {gato_1.hacer_sonido()} ")

cuenta_1 = CuentaBancaria("Facundo Bustamante", 500000)
cuenta_1.obtener_saldo()
cuenta_1.depositar_saldo(150000)
cuenta_1.retirar_saldo(250000)