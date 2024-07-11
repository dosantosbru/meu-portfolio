import os

def limpa():
    os.system('cls')

limpa()

temperatura = 100

if temperatura > 100:
    agua_ferve = True
    evapora = 'muito rápido'
    print(f'Com a temperatura em {temperatura} Celsius, a agua ferve!\n E também evapora {evapora}')
else:   
    print('A temperatura está baixa, a aguá não irá ferver')

   