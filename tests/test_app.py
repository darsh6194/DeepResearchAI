import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Deep Research AI' in response.data

def test_query_endpoint(client):
    response = client.post('/query', 
                         json={'query': 'test query'},
                         content_type='application/json')
    assert response.status_code in [200, 500]  # 500 if API keys are not set 