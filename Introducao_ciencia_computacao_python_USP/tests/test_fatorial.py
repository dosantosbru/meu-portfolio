import os
import math
import pytest


def fatorial(x):
    return math.factorial(x)


"""
def fatorial(x):
    i = fat = 1
    while i <= x:
        fat *= i
        i += 1
    return fat
"""


def test_fatorial5():
    assert fatorial(5) == 120
