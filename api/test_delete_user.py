import requests
import pytest

from config import USER_URL
from messages import WRONG_STATUS_CODE
from user import create_user

@pytest.mark.parametrize("user_name", ['den12', 'pol12', 'tol12'])
def test_delete_user(user_name):
    create_user(user_name)
    url = USER_URL + f'/{user_name}'
    payload = {}
    headers = {
     'accept': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200, WRONG_STATUS_CODE
    
    url = USER_URL + '/' + user_name
    payload = {}
    headers = {
    'accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 404, WRONG_STATUS_CODE