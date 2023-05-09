from fastapi.testclient import TestClient
from main import app,Registration
from fastapi import Response

client = TestClient(app) 


def test_Registration():
    # payload = Response.set_cookie(key="X-Authorization", value='Mahesh', httponly=True)
    response = client.post("/submitform",data={'user':'Mahesh'})
    assert response
    assert response.status_code == 200
    
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    
def test_question():
    response = client.get("/question")
    assert response.status_code == 200
    
def test_sendUserDetails():
    response = client.get("/user")
    assert response.status_code == 200