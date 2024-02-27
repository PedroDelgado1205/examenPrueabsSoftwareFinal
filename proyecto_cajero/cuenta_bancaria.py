class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def realizar_deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            return False

    def realizar_retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False
