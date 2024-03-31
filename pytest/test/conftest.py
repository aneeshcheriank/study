# we can define the fixtures as global here

import pytest
import src.class_app as app

@pytest.fixture
def global_rectangle():
    return app.Rectangle(24, 34)