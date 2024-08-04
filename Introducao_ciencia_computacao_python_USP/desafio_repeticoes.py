import os
import math


def fatorial(x):
    return math.factorial(x)


a = int(input('Digite um número de 1 a 10: '))

while a <= 10:
    resultado = fatorial(a)
    print(f'O fatorial de {a} é: {resultado}')
    a += 1
