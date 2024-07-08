decrescente = True

anterior = int(input("Digite o primeiro número da sequência: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite um valor: "))
    if valor != 0:
        if valor <= anterior:
            decrescente = True
        else:
            decrescente = False
    anterior = valor

if decrescente:
    print("A sequência é decrescente.")
else:
    print("A sequência não é decrescente.")
