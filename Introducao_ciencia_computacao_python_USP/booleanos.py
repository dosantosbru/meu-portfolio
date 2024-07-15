import os

def limpa_console():
    os.system ('cls')
x = 4
y = 10

limpa_console()

def valida_cond (x,y):

    if (x > 0) and (y ** 2 > 100):
        return True
    else:
        return False

resultado = valida_cond(x,y)
print(f'O Resultado da condição é:  {resultado}')


"""
    operadores lógicos 
    And - e 
    OR - ou
    NOT - inverte o valor de um booleano
    
"""