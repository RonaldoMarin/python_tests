import unittest

class Pilha:
    def __init__(self) -> None:
        self.items = []
    
    def empilhar(self, item):
        self.items.append(item)
    
    def desempilhar(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self) -> int:
        return len(self.items) == 0

class TestPilha(unittest.TestCase):
    pilha = Pilha()

    def test_empilhar(self):
        self.pilha.empilhar(4)
        self.assertEqual(self.pilha.items, [4])
        
    
    def test_desempilhar(self):
       self.pilha.empilhar(4)
       item = self.pilha.desempilhar()
       self.assertEqual(item, 4)
       self.assertEqual(self.pilha.items, [])

    def test_is_empty(self):
        self.pilha.desempilhar()
        self.assertTrue(self.pilha.is_empty())
        self.pilha.empilhar(1)
        self.assertFalse(self.pilha.is_empty())

if __name__ == '__main__':
    unittest.main()