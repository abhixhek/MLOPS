import pytest

def test_generic() :
    a = 30
    b = 40
    assert a != b

class NotInRange(Exception):
    def __init__(self, message = "Value Not in Range"):
        self.message = message
        super().__init__(self.message)

def test_generic1():
    a = 5
    with pytest.raises(ValueError):
        if a not in range(10,20):
            raise NotInRange
