import os
import math

# Aula: repetições encaixadas 22/07/2024

linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        produto = linha * coluna
        # produto:4 garante que cada número ocupe pelo menos 4 espaços de largura
        print(f'{produto:4}', end=' ')
        coluna += 1

    print()
    linha += 1
    coluna = 1
