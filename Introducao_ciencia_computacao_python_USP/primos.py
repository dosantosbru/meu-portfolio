from sympy import isprime

numero_primo = int(input('Digite um número inteiro: '))

if isprime(numero_primo):
    print(f'O número informado é um número primo')
else:
    print('O número informado não é um número primo')

# print(f'O número {numero_primo} é primo? \n{isprime(numero_primo)}')
