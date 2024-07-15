"""


## a*x**2 + b*x + c = 0 

delta > 0 
   imprimir as duas raizes 

delta < 0
 não possui raiz real 

 delta = 0 
    a raíz é e qual raíz
"""

import os
import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

def bhaskara(a,b,c):

    delta = b ** 2 - 4 * a * c

    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)

    return raiz1,raiz2

raizes = bhaskara(a,b,c)

print("As raízes da equação são:", raizes)