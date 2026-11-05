import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_index_status(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_json(client):
    response = client.get('/')
    assert response.is_json
    assert response.mimetype == 'application/json'


def test_index_tasks(client):
    response = client.get('/')
    assert response.get_json() == [
        {'id': 1, 'title': 'Estudar Docker'},
        {'id': 2, 'title': 'Criar o pipeline'},
    ]


def test_unknown_route(client):
    response = client.get('/rota-inexistente')
    assert response.status_code == 404
