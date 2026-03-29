from main import add, subtract

def test_add():
    add(1,2)
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    subtract(10, 5)
    assert(10, 5) == 5
    assert(0, 5) == -5