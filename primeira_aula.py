import os
import math

os.system('cls')
numero = int(input('Digite um número para o cálculo fatorial: '))

def opcao_invalida():
    if numero != int:
        print('O cálculo fatorial é apenas para número inteiros, digite Enter para tentar novamente')
        numero()

    elif numero == float:
        print('O cálculo fatorial é apenas para número inteiros, digite Enter para tentar novamente')
        numero()

def imprimir_resultado(equacao):
    print(f'O fatorial de {numero} é:  {equacao}')
    print()

equacao = math.factorial(numero)
imprimir_resultado(equacao)