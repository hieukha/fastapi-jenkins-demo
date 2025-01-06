from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test cases for /get_version
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test cases for /check_prime/{number}
def test_check_prime_prime_number():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

def test_check_prime_not_prime_number():
    response = client.get("/check_prime/10")
    assert response.status_code == 200
    assert response.json() == {"number": 10, "is_prime": False}

def test_check_prime_edge_case_1():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

def test_check_prime_edge_case_2():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_large_prime():
    response = client.get("/check_prime/101")
    assert response.status_code == 200
    assert response.json() == {"number": 101, "is_prime": True}

def test_check_prime_large_not_prime():
    response = client.get("/check_prime/100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

def test_check_prime_negative_number():
    response = client.get("/check_prime/-5")
    assert response.status_code == 200
    assert response.json() == {"number": -5, "is_prime": False}

def test_check_prime_zero():
    response = client.get("/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_float_number():
    response = client.get("/check_prime/4.5")
    assert response.status_code == 422  # FastAPI sẽ trả lỗi do float không phải kiểu int

def test_check_prime_string_input():
    response = client.get("/check_prime/abc")
    assert response.status_code == 422  # FastAPI sẽ trả lỗi do input không hợp lệ
