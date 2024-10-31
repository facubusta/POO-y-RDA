class CuentaBancaria:

    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.__saldo = saldo
    
    def obtener_saldo(self) ->None:
        print(f"{self.titular} su saldo actual es de ${self.__saldo}")
    
    def depositar_saldo(self, cantidad:float) ->None:
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"{self.titular} su depósito de ${cantidad} fue exitoso. Su saldo actual es de: ${self.__saldo}")
        else:
            print("El monto a depositar es invalido, por favor ingrese un monto positivo.")
    
    def retirar_saldo(self, cantidad: float) ->None:
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"{self.titular} su retiro de ${cantidad} fue exitoso. Su saldo actual es de: ${self.__saldo} ")
        elif cantidad > self.__saldo:
            print("Fondos insuficiente")
        else:
            print("Ingresa una cantidad positiva")
        