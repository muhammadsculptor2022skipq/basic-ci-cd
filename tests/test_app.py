# tests/test_app.py
from app import app
from app.service import ToDoService
import json

def test_health_check():
    client = app.test_client()
    response = client.get('/health')

    assert response.status_code == 200
    assert response.json == {'status': 'ok'}

def test_add_todo():
    client = app.test_client()

    # Assuming your API has an endpoint for adding a todo item
    todo_data = {'title': 'Test Todo', 'completed': False}

    response = client.post('/todo', json=todo_data)

    assert response.status_code == 200  # Adjust the status code based on your implementation
    assert response.json['title'] == 'Test Todo'
    assert response.json['completed'] == False

def test_get_todos():
    client = app.test_client()

    # Assuming your API has an endpoint for fetching all todo items
    response = client.get('/todo')

    assert response.status_code == 200
    todos = response.json  # Adjust the structure based on your implementation

    # You can add more assertions based on the expected structure of your response
    assert isinstance(todos, list)
