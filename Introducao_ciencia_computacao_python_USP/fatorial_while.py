'''
Dado um número inteiro N (N > 1), imprima sua decomposição em fatores primos e a quantidade de vezes que cada fator aparece.

primos de 1 a 10 [2,3,5 e 7]

exemplo:

30=2*3*5

Aqui, 2, 3 e 5 são todos números primos. Portanto, a decomposição em fatores primos de 30 é 2, 3 e 5, cada um com multiplicidade 1.

'''

import os
import math

N = int(input('Digite um número inteiro maior que 1: '))

fatores_primos = 2
multiplicidade = 0

while N > 1:
    while N % fatores_primos == 0:
        multiplicidade = multiplicidade + 1
        N = N // fatores_primos
    if multiplicidade > 0:
        print(
            f'O fator de {fatores_primos} tem multiplicidade {multiplicidade}')
    fatores_primos = fatores_primos + 1
    multiplicidade = 0
