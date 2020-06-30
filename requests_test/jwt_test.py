import requests


def login():
    url = 'http://127.0.0.1:8000/api-token-auth/'
    user_info = {"username": "admin", "password": "fang"}
    login_response = requests.post(url, json=user_info)
    return login_response.json()


if __name__ == '__main__':
    print(login())
