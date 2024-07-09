import math

def fatorial(valor:int) -> int:
    if valor < 0 or isinstance(valor, float):
        return TypeError
    elif valor == 0:
        return 1
    valor_fatorial = math.factorial(valor)
    return valor_fatorial


