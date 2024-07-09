import unittest
from fatorial import fatorial

class TesteFatorialDeUmNumero(unittest.TestCase):
    def test_fatorial_positivo(self):
        resultado = fatorial(valor=3)
        self.assertEqual(6, resultado)

    def test_fatorial_zero(self):
        resultado = fatorial(valor=0)
        self.assertEqual(1, resultado)


    def test_fatorial_negativo(self):   
        resultado = fatorial(valor=3.3)
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()