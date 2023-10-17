import requests
import json
import random

from config import USER_URL


def create_user(user_name:str):
    url = USER_URL
    payload = json.dumps({
    "id": 1894,
    "username": user_name,
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
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200, response.text


def delete_user(user_name:str):
    url = USER_URL + '/' + user_name
    payload = {}
    headers = {
     'accept': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200, response.text


def get_user(user_name:str):
    url = USER_URL + '/' + user_name
    payload = {}
    headers = {
    'accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200, response.text
    return response.json()
