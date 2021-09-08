from sqlalchemy.orm import Session
from db.crud.jobs import create_new_job, retrieve_job
from schemas.jobs import JobCreate
from test.utils.users import create_random_owner
from test.utils.jobs import create_sample_job


def test_retrieve_job_by_id(db_session: Session):
    """Test retrieving job from db"""
    owner = create_random_owner(session=db_session)
    job = create_sample_job(owner, db_session)
    retrieved_job = retrieve_job(job_id=job.id, session=db_session)
    assert retrieved_job.id == job.id
    assert retrieved_job.title == job.title
