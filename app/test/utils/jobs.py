from sqlalchemy.orm import Session
from db.crud.jobs import create_new_job, retrieve_job
from schemas.jobs import JobCreate
from db.models.users import User
from db.models.jobs import Job


sample_job_schema = JobCreate(title='test title', company='test company',
                              company_url='sample.url.com', location='US/NY',
                              description='Sample description')


def create_sample_job(owner: User, db_session: Session,
                      job_schema: JobCreate = sample_job_schema) -> Job:
    job = create_new_job(job=job_schema, session=db_session, owner_id=owner.id)
    return job
