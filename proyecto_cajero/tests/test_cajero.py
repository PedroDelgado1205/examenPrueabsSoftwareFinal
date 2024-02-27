import unittest
from persona import Persona
from cuenta_bancaria import CuentaBancaria
from cajero_automatico import CajeroAutomatico

class TestCajeroAutomatico(unittest.TestCase):
    def setUp(self):
        self.persona1 = Persona("Juan", "Perez", "12345678")
        self.persona2 = Persona("Maria", "Gonzalez", "87654321")
        self.cuenta1 = CuentaBancaria(self.persona1, 1000)
        self.cuenta2 = CuentaBancaria(self.persona2, 500)
        self.cajero = CajeroAutomatico()
        self.cajero.agregar_cuenta(self.cuenta1)
        self.cajero.agregar_cuenta(self.cuenta2)

    def test_consultar_saldo(self):
        self.assertEqual(self.cajero.consultar_saldo("12345678"), 1000)
        self.assertEqual(self.cajero.consultar_saldo("87654321"), 500)
        self.assertEqual(self.cajero.consultar_saldo("11111111"), "Cuenta no encontrada")

    def test_realizar_deposito(self):
        self.assertTrue(self.cajero.realizar_deposito("12345678", 500))
        self.assertEqual(self.cajero.consultar_saldo("12345678"), 1500)
        self.assertFalse(self.cajero.realizar_deposito("87654321", -200))

    def test_realizar_retiro(self):
        self.assertTrue(self.cajero.realizar_retiro("87654321", 200))
        self.assertEqual(self.cajero.consultar_saldo("87654321"), 300)
        self.assertFalse(self.cajero.realizar_retiro("12345678", 2000))

if __name__ == '__main__':
    unittest.main()
