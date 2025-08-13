import pytest

def add(a, b):
    return a + b
def mul(a, b):
    return a * b

def test_positive():
    assert add(2, 3) == 5
    assert mul(2, 4) == 6

def test_negative():
    assert add(-1, -4) == -5
    assert mul(-1, -4) == 4

def test_add_zero():
    assert add(0, 3) == 0

def test_add_debug():
    print("Running add debug test ")
    assert add(1, 1) == 2