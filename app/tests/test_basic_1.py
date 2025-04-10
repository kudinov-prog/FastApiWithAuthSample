import json
import requests
import pytest
from fastapi.testclient import TestClient
from app.main import app as appl


client = TestClient(appl)


def test_read_main():
    """ Тестирование главной страницы """
    
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
                                "message": "Добро пожаловать! Проект создан для сообщества 'Легкий путь в Python'.",
                                "community": "https://t.me/PythonPathMaster",
                                "author": "Яковенко Алексей"
                                }


def test_login():
    """ Тестирование успешного входа зарегестрированного пользователя"""

    data = {"email":"user1@example.com", "password": "password"}
    response = client.post(
        "auth/login",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
        )
    assert response.status_code == 200
    assert response.json() == {'ok': True, 'message': 'Авторизация успешна!'}


def test_logout():
    """ Тестирование успешного выхода пользователя из системы"""

    response = client.post("auth/logout")
    assert response.status_code == 200
    assert response.json() == {'message': 'Пользователь успешно вышел из системы'}


def test_me():
    """ Проверка авторизованного пользователя """
    cookies = {"user_access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMSIsImV4cCI6MTc0NDExNTM2MCwidHlwZSI6ImFjY2VzcyJ9.d6JZdqwORRWmAKW65holdMKPXqGrKnsu1EGNfRc53Ro"
                }

    response = requests.get(
        "http://127.0.0.1:8000/auth/me/",
        cookies=cookies
        )
    
    assert response.status_code == 200
    assert response.json()['email'] is not None


def test_all_users():
    """ Тестирование получения всех пользователей """

    cookies = {"user_access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMSIsImV4cCI6MTc0NDExNTM2MCwidHlwZSI6ImFjY2VzcyJ9.d6JZdqwORRWmAKW65holdMKPXqGrKnsu1EGNfRc53Ro"
                }
    response = requests.get(
        "http://127.0.0.1:8000/auth/all_users/",
        cookies=cookies
        )
    
    assert response.status_code == 200
    assert len(response.json()) >= 1
