import pytest
import time
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

# we can mark a test as slow
@pytest.mark.slow
def test_very_slow():
    time.sleep(10)
    result = app.divide(10, 2)
    assert result == 5



# deactivate the virtual environment
# --> deactivate

