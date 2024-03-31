import pytest
import math
import src.class_app as app

class TestCircle:

    def setup_method(self, method):
        print(f'setting up: {method}')
        self.circle = app.Circle(10)

    def teardown_mehtod(self, method):
        print(f'tearning down up: {method}')

    def test_radious(self):
        assert self.circle.radius == 10
    
    def test_area(self):
        area = self.circle.area()
        assert area == math.pi * 10 ** 2

    def test_perimeter(self):
        perimeter = self.circle.perimeter()
        assert perimeter == 2 * math.pi * 10
