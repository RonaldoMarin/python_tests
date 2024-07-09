import unittest
from busca_binaria import busca_binaria

class TesteBuscaBinaria(unittest.TestCase):
    def test_encontrado(self):
        lista = [2, 3, 4, 9, 21, 100, 32]
        elemento = 9
        resultado = busca_binaria(lista, elemento)
        self.assertEqual(3, resultado)
        
    
    def test_nao_encontrado(self):
        lista = [2, 3, 4, 9, 21, 100, 32]
        elemento = 12
        resultado = busca_binaria(lista, elemento)
        self.assertEqual(-1, resultado)
    
if __name__ == '__main__':
    unittest.main()