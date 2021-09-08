import json

from fastapi import status
from fastapi.testclient import TestClient
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session
from test.utils.jobs import create_sample_job
from test.utils.users import create_random_owner


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
    assert response.status_code == status.HTTP_201_CREATED


def test_retrieve_job_by_id(client: TestClient, db_session: Session):
    """Tests retrieving a job by id endpoint"""
    owner = create_random_owner(session=db_session)
    test_job = JobCreate(title='test retrieve', company='test company',
                         company_url='sample.url.com',
                         location='US/NY',
                         description='Sample description')
    job = create_sample_job(owner, db_session, job_schema=test_job)
    response = client.get(f'/job/{job.id}')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['title'] == 'test retrieve'


def test_retrieve_not_found_job(client: TestClient):
    """Tests retrieving not found job fails"""
    response = client.get(f'/job/123')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_retrieve_invalid_id_job_fails(client: TestClient):
    """Tests retrieving invalid job id fails"""
    response = client.get(f'/job/-1')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
