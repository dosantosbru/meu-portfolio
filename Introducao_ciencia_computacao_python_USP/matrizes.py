def matriz(numero_linhas, numero_colunas, valor):

    matriz = []
    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            linha.append(valor)

        matriz.append(linha)
        
    return matriz


minha_matriz = matriz(3, 3, 0)

for linha in minha_matriz:
    print(linha)
