import requests


def test_response():
    data = {"key": "value"}
    url = "http://127.0.0.1:5000/test_response"
    response = requests.post(url, data)
    assert response.status_code == 200
    assert response._content == b"SUCCESS"


def test_payload():
    data = {"key": "value"}
    url = "http://127.0.0.1:5000/test_payload"
    response = requests.post(url, data)
    assert response.status_code == 200
    assert response.json() == data
