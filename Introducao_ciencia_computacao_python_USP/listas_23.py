import os
import math

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


pares = [2, 4, 6, 8, 10]


# criando um clone da lista primos
primos2 = primos[:]

# A função principal do script


def main():
    # primos[1:4] cria uma nova lista a partir da lista primos,
    # que vai percorrer os indices de 1 a 4 ou seja os itens 3, 5 e 7
    print(f'{primos[1:4], primos2}')


if __name__ == "__main__":
    main()
