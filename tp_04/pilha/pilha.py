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

