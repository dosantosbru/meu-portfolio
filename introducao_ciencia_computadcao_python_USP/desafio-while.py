import os
import math

N = 6532
soma = 0
numero = N

while numero > 0:
    digito = numero % 10  # obtém o último dígito
    soma += digito        # adiciona o dígito à soma
    numero //= 10         # remove o último dígito do número

print(f"A soma dos dígitos de {N} é: {soma}")

