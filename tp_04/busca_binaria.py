import unittest

def busca_binaria(lista:list, elemento:int) -> bool:
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio  # Elemento encontrado, retorna o índice
        elif lista[meio] < elemento:
            esquerda = meio + 1  # Ignora a metade esquerda
        else:
            direita = meio - 1  # Ignora a metade direita
    
    return -1  # Elemento não encontrado

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