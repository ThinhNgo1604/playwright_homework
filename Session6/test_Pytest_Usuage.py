import pytest

def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -4) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_debug():
    print("Running add debug test ")
    assert add(1, 1) == 2