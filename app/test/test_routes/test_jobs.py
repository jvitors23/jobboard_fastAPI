import json
from fastapi import status


def test_job_creation(client):
    """Tests job creation endpoint"""
    data = {
        'title': 'Python Developer',
        'company': 'Google',
        'company_url': 'https://www.google.com',
        'location': 'USA/NY',
        'description': 'Test job',
        'date_posted': '2022-07-20'
    }

    response = client.post('/job/create-job', json.dumps(data))
    assert response.status_code == status.HTTP_200_OK
