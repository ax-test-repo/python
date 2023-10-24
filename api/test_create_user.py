import requests
import json
import random
import pytest

from jsonschema import validate

from config import USER_URL
from schemas import CREATE_USER_SCHEMA

def teardown_function():
    url = USER_URL + '/djarin2'
    payload = {}
    headers = {
     'accept': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200, response.text

def test_create_user():
    id = random.randint(1000, 2000)
    payload = json.dumps({
    "id": id,
    "username": "djarin2",
    "firstName": "Din",
    "lastName": "Djarin",
    "email": "din.djarin@mando.com",
    "password": "Great123",
    "phone": "01299145399",
    "userStatus": 0
    })
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url = USER_URL, headers=headers, data=payload)
    assert response.status_code==200, 'Некорректный статус'
    data = response.json()
    assert data["message"] == str(id), 'id пользователя не совпадает'
    validate(data, CREATE_USER_SCHEMA)