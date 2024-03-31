import pytest
import src.class_app as app

# pytest fixtures
@pytest.fixture
def my_rectangle():
    return app.Rectangle(10, 20)

# def test_area():
#     rectangle = app.Rectangle(10, 20)
#     assert rectangle.area() == 10*20

# def test_perimiter():
#     rectangle = app.Rectangle(10, 20)
#     assert rectangle.perimeter() == 2*(10+20)


def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20

def test_perimiter(my_rectangle):
    assert my_rectangle.perimeter() == 2*(10+20)

def test_area_global(global_rectangle):
    assert global_rectangle.area() == global_rectangle.length * global_rectangle.width
