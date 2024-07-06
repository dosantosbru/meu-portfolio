import os

def limpar_console():
    os.system('cls')

    #Y é um número real, Em Python, qualquer número que inclua um ponto decimal é considerado um float
    y = 2.4 
    
    x = 5 * 5 + y
    #converte o resultado para um número inteiro 
    soma = int(x + y) 

    frase = 'O resultado da soma é: '
    print(f'{frase}{soma}')
    print(f' O comprimento da variavel y é: {len(str(y))}')

    #print('A Soma dos números é ', soma)

limpar_console()

