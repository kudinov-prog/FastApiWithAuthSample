import requests

url = 'http://127.0.0.1:8000/auth/me/'

cookies = {"user_access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMSIsImV4cCI6MTc0NDExNTM2MCwidHlwZSI6ImFjY2VzcyJ9.d6JZdqwORRWmAKW65holdMKPXqGrKnsu1EGNfRc53Ro"
                }

response = requests.get(
        "http://127.0.0.1:8000/auth/me/",
        cookies=cookies
        )
print(response.json()['email'])
#assert response.status_code == 200
#assert response.json() == {'email': "user1@example.com"}