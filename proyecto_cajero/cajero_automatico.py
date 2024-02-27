from cuenta_bancaria import CuentaBancaria


class CajeroAutomatico:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, cuenta):
        if isinstance(cuenta, CuentaBancaria):
            self.cuentas[cuenta.titular.dni] = cuenta
            return True
        else:
            return False

    def consultar_saldo(self, dni):
        if dni in self.cuentas:
            return self.cuentas[dni].consultar_saldo()
        else:
            return "Cuenta no encontrada"

    def realizar_deposito(self, dni, cantidad):
        if dni in self.cuentas:
            return self.cuentas[dni].realizar_deposito(cantidad)
        else:
            return False

    def realizar_retiro(self, dni, cantidad):
        if dni in self.cuentas:
            return self.cuentas[dni].realizar_retiro(cantidad)
        else:
            return False
