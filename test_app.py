from app import add, devide
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_devide():
    assert devide(6, 3) == 2
    assert devide(5, 2) == 2.5
def test_devide_by_zero():
    assert devide(10, 0) == 5 