n = int(input('Digite um número inteiro: '))


def primo(x):
    fator = 2
    while x % fator != 0 and fator < x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


while n > 0:
    if primo(n):
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')
    n = int(input('Digite um número inteiro: '))
