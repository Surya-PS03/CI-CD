from fastapi.testclient import TestClient
from main import app
client = TestClient(app)



def test_get_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"message":"Server is fine and running"}

def test_hello():

    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"message":"hello world!"}

def test_get_name():
    response = client.get("/get_name")
    assert response.status_code == 200
    assert response.json() == {"message":"My name is Surya"}