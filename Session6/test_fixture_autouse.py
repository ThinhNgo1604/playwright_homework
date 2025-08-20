import pytest
@pytest.fixture(autouse=True)
def my_fixture():
    print("🎯 This runs before each test")

def test_1():
    print("🔹 test_1")

def test_2():
    print("🔹 test_2")