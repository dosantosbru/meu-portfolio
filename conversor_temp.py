import os

def limpar_console():
    os.system('cls')

temperaturaF = input('Digite uma temperatura em Fahrenheit: ')

temperaturaC  = (float(temperaturaF) - 32) * 5 / 9
limpar_console()

print(f'A temperatura em Celsius é: {int(temperaturaC)}') 

