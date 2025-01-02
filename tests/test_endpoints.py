import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def auth_header():
    response = client.get("/token")
    token = response.json()["token"]
    return {"Authorization": f"Bearer {token}"}

# GET /token
def test_get_token():
    response = client.get("/token")
    assert response.status_code == 200
    assert "token" in response.json()

# GET /tasks
def test_get_tasks(auth_header):
    response = client.get("/tasks", headers=auth_header)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
   
# GET /tasks/{id} 
def test_get_task_by_id(auth_header):
    payload = {
        "title": "Teste",
        "description": "Realizar testes usando Pytest",
        "state": "pendente"
    }
    create_response = client.post("/tasks", json=payload, headers=auth_header)
    task_id = create_response.json()["id"]
    
    response = client.get(f"/tasks/{task_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

# POST /tasks
def test_create_task(auth_header):
    payload = {
        "title": "Teste",
        "description": "Realizar testes usando Pytest",
        "state": "pendente"
    }
    
    response = client.post("/tasks", json=payload, headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["state"] == payload["state"]

# PUT /tasks
def test_update_task(auth_header):
    payload = {
        "title": "Teste para atualizar",
        "description": "Descrição do teste atualizada",
        "state": "pendente"
    }
    create_response = client.post("/tasks", json=payload, headers=auth_header)
    task_id = create_response.json()["id"]

    update_payload = {
        "title": "Updated Test",
        "state": "em andamento"
    }
    response = client.put(f"/tasks/{task_id}", json=update_payload, headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_payload["title"]
    assert data["state"] == update_payload["state"]
 
# DELETE /tasks   
def test_delete_task(auth_header):
    payload = {
        "title": "Teste para deletar",
        "description": "Descrição do teste para deletar",
        "state": "pendente"
    }
    create_response = client.post("/tasks", json=payload, headers=auth_header)
    task_id = create_response.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted"

    # Verify deletion
    get_response = client.get(f"/tasks/{task_id}", headers=auth_header)
    assert get_response.status_code == 404