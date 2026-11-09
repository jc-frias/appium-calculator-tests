# test_api.py
import requests
import pytest

USERS_URL = "https://jsonplaceholder.typicode.com/users/"
POST_URL = "https://jsonplaceholder.typicode.com/posts/"

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

def test_data_send():
    data = {"title": "mi primer post", "body": "probando", "userId": 1}
    response = requests.post(POST_URL, json=data)
    status_code = response.status_code
    print(status_code)
    expected_code = 201
    assert status_code == expected_code, f"Unexpected code response, got: {status_code}; Expected: {expected_code}"
    post_info = response.json()
    title = post_info["title"]

    assert title == data["title"], f"Unexpected title, got: {title}; Expected: {data['title']}"
    assert "id" in post_info, "Response does not include the post id"

@pytest.mark.parametrize("data",
                         [({}),({"title": 123}), ({"title":"abc"*1000})])
@pytest.mark.xfail(reason="Test site, negative responses are not applicable", strict=True)
def test_negative_responses(data):
    negative_codes = [400, 401, 403, 404, 422]
    response = requests.post(POST_URL, json=data)
    status_code = response.status_code
    print(status_code)
    assert status_code in negative_codes, f"Site is accepting invalid info, got: {status_code}; Expected: {negative_codes}"