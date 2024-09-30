import os
import math
import pytest


def fatorial(x):
    return math.factorial(x)


"""
loop que calcula o fatorial de x, quando não se quer usar a biblioteca python
def fatorial(x):
    i = fat = 1
    while i <= x:
        fat *= i
        i += 1
    return fat
"""


def test_fatorial5():
    assert fatorial(5) == 120
