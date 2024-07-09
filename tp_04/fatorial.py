import unittest
import math

class CalcularFatorial:
    def fatorial(valor:int) -> int:
        if valor < 0 or isinstance(valor, float):
            return TypeError
        elif valor == 0:
            return 1
        valor_fatorial = math.factorial(valor)
        return valor_fatorial


class TesteFatorialDeUmNumero(unittest.TestCase):
    def test_fatorial_positivo(self):
        resultado = CalcularFatorial.fatorial(valor=3)
        self.assertEqual(6, resultado)

    def test_fatorial_zero(self):
        resultado = CalcularFatorial.fatorial(valor=0)
        self.assertEqual(1, resultado)


    def test_fatorial_negativo(self):   
        resultado = CalcularFatorial.fatorial(valor=3.3)
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()