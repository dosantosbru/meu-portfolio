import os
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def bhaskara(a,b,c):

    delta = b ** 2 - 4 * a * c
    

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        raizes = (x1,x2)
        print(f"As raízes são: {raizes}")

    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"A única raiz é: {x1}")
    else:
        print("A equação não possui raízes reais.")

bhaskara(a,b,c)
