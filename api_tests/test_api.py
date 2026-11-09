# test_api.py
import requests
import pytest

USERS_URL = "https://jsonplaceholder.typicode.com/users/"

@pytest.mark.parametrize("user, expected_code",
                         [(1,200),
                          (10,200),
                          (11,404),
                          (9999,404),
                          (0,404)])
def test_user_response(user, expected_code):
    url = f"{USERS_URL}{user}"
    response = requests.get(url)
    status_code = response.status_code
    assert status_code == expected_code, f"Unexpected status code, got: {status_code}; Expected {expected_code}"


"""
def test_web_response_and_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    status_code = response.status_code
    print(f"\n{status_code}")
    assert status_code == 200, f"Unexpected status code, got: {status_code}; Expected 200"

    web_info = response.json()
    name = web_info["name"]
    print(name)
    assert name == "Leanne Graham", f"Name does not match, got: {name}; Expected: Leanne Graham"



def test_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    status_code = response.status_code
    print(f"\n{status_code}")
    assert status_code == 404, f"Unexpected status code, got: {status_code}; Expected 404"
"""