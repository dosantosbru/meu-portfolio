import os
import math
import pytest


def fatorial(x):
    return math.factorial(x)


def test_fatorial5():
    assert fatorial(5) == 120
