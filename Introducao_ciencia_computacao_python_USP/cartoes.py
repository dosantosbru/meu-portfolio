import os
import math

Numero = int(input("Digite um número"))
digitos_iguais = False


while Numero != 0:

    ultimo_digito = Numero % 10

    # Remove o dígito atual do número
    Numero = Numero // 10

    proximo_digito = Numero % 10

    if ultimo_digito == proximo_digito:
        digitos_iguais = True
        break

if digitos_iguais:
    print("Tem adjacente igual")
else:
    print("Não tem adjacente igual")
