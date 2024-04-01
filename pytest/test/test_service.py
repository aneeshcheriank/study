import pytest
import src.service as service
import unittest.mock as mock

# not working, need to check
@mock.patch("src.service, get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.retrun_value = 'Mocked Alice'
    user_name = service.get_user_from_db(1)

    assert user_name == 'Mocked_Alice'
