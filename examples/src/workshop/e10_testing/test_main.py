import pytest
from starlette.testclient import TestClient

from . import main


@pytest.fixture
def our_test_client():
    app = main.app
    client = TestClient(app)
    return client



def test_hello_name_orell(our_test_client):
    response = our_test_client.get("/hello/Orell")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Orell"

def test_hello_name_alice(our_test_client):
    response = our_test_client.get("/hello/alice")

    assert response.status_code == 400


def get_testing_db() -> dict:
    return {
        "Alice": 25,
        "Bob": 31
    }

@pytest.fixture
def database_test_client():
    app = main.app
    app.dependency_overrides[main.get_db] = get_testing_db
    client = TestClient(app)
    return client

def test_get_user(database_test_client):
    response = database_test_client.get("/name/Alice")

    assert response.status_code == 200
    assert response.json()["Alice"] == 25
