import json
from fastapi import status


def test_create_user(client):
    """Test user creation endpoint"""
    data = {'username': 'jose123', 'email': 'jose@gmail.com',
            'password': '1231231235'}
    response = client.post('/user/', json.dumps(data))

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['email'] == data['email']
    assert response.json()['is_active']
