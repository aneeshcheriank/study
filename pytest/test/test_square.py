import pytest
import src.class_app as app

@pytest.mark.parametrize("side_length, expected_area", [(2, 4), (5, 25), (9, 81), (10, 100)])
def test_multiple_square_areas(side_length, expected_area):
    assert app.Square(side_length).area() == expected_area