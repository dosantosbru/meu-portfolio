import os
import math
n = 6
k = 4
# k precisa ser <= n


def fatorial(x):
    return math.factorial(x)


def binomial(n, k):
    binomial = fatorial(n) // (fatorial(k) * fatorial(n-k))
    return binomial


resultado = binomial(n, k)

print(f'O resultado binomial é: {resultado}')

# aplicando testes no cálculo fatorial


def teste_fatorial():
    if fatorial(1) == 1:
        print(f'O código está correto para {fatorial(1)}')
    else:
        print(f'O código está incorreto para: {fatorial(1)}')
    if fatorial(2) == 2:
        print(f'O código está correto para {fatorial(2)}')
    else:
        print(f'O código está incorreto para: {fatorial(2)}')
    if fatorial(0) == 1:  # por definição matemática o fatorial de (0) é 1
        # aqui apliquei apenas o zero por extenso, pois, se eu passar o parâmetro ele irá imprmir o resultado que é 1
        print(f'O código está correto para zero')
    else:
        print(f'O código está incorreto para: {fatorial(0)}')


teste_fatorial()
