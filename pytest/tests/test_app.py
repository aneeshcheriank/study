import pytest

import src.app as app

def test_add_numbers():
    result = app.add_numbers([1, 2, 3])
    assert result == 6

def test_mul_numbers():
    result = app.mul_numbers([1, 2, 3])
    assert result == 6

# we may need to test num/0
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = app.divide(10, 0)



# deactivate the virtual environment
# --> deactivate

