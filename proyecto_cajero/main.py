from persona import Persona
from cuenta_bancaria import CuentaBancaria
from cajero_automatico import CajeroAutomatico

# Crear algunas personas y cuentas bancarias
persona1 = Persona("Pedro", "Delgado", "12345678")
persona2 = Persona("Miguel", "Bravo", "87654321")
cuenta1 = CuentaBancaria(persona1, 1500)
cuenta2 = CuentaBancaria(persona2, 460)

# Crear un cajero automático y agregar las cuentas
cajero = CajeroAutomatico()
cajero.agregar_cuenta(cuenta1)
cajero.agregar_cuenta(cuenta2)

# Simulación de operaciones en el cajero automático
print("Saldo de la cuenta de Juan Perez:", cajero.consultar_saldo("12345678"))
print("Saldo de la cuenta de Maria Gonzalez:", cajero.consultar_saldo("87654321"))

cajero.realizar_deposito("12345678", 500)
print("Saldo de la cuenta de Juan Perez después del depósito:", cajero.consultar_saldo("12345678"))

cajero.realizar_retiro("87654321", 200)
print("Saldo de la cuenta de Maria Gonzalez después del retiro:", cajero.consultar_saldo("87654321"))