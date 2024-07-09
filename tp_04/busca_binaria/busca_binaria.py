def busca_binaria(lista:list, elemento:int) -> bool:
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio  
        elif lista[meio] < elemento:
            esquerda = meio + 1  
        else:
            direita = meio - 1  
    return -1  

