from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_div():
    assert divide(6, 2) == 3

def test_sub():
    assert subtract(3, 2) == 1

def test_mul():
    assert multiply(6, 2) == 12
