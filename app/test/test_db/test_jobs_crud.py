from sqlalchemy.orm import Session
from db.crud.jobs import create_new_job, retrieve_job
from schemas.jobs import JobCreate
from test.utils.users import create_random_owner


def test_retrieve_job_by_id(db_session: Session):
    """Test retrieving job from db"""
    title = 'test title'
    company = 'test company'
    company_url = 'testcompany.com'
    location = 'USA,NY'
    description = 'Test job'
    owner = create_random_owner(session=db_session)
    job_schema = JobCreate(title=title, company=company,
                           company_url=company_url, location=location,
                           description=description)
    job = create_new_job(job=job_schema, session=db_session, owner_id=owner.id)
    retrieved_job = retrieve_job(id=job.id, session=db_session)
    assert retrieved_job.id == job.id
    assert retrieved_job.title == job.title
