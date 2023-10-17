import requests
import json
import pytest

from config import USER_URL
from utils.messages import WRONG_STATUS_CODE, WRONG_USER_ID
from utils.user_utils import delete_user, create_user, get_user

user_name = "djarin21"
url = USER_URL + '/' + user_name

def teardown_function():
    print("teardown_function")
    delete_user(user_name)

def setup_function():
   print("setup_function")
   create_user(user_name)

def test_get_user():
    print("test_get_user")
    payload = {}
    headers = {
    'accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200, WRONG_STATUS_CODE
    assert response.json()["username"] == user_name

def test_update_user():
    print('test_update_user')
    new_first_name = "Din21"
    payload = json.dumps({
    "id": 1894,
    "username": user_name,
    "firstName": new_first_name,
    "lastName": "Djarin2",
    "email": "din.djarin@mando.com",
    "password": "Great123",
    "phone": "01299145399",
    "userStatus": 0
    })
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 200, WRONG_STATUS_CODE
    assert response.json()["message"] == "1894", WRONG_USER_ID
    
    user = get_user(user_name)
    assert user["username"] == user_name; 
    assert user["firstName"] == new_first_name; 
    assert user["id"] == 1894;
