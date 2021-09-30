from sqlalchemy.orm import Session
from typing import List
from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, session: Session, owner_id: int) -> Job:
    job = Job(**job.dict(), owner_id=owner_id)
    session.add(job)
    session.commit()
    session.refresh(job)
    return job


def retrieve_job(job_id: int, session: Session) -> Job:
    job = session.query(Job).filter(Job.id == job_id).first()
    return job


def retrieve_all_jobs(session: Session) -> List[Job]:
    jobs = session.query(Job).filter(Job.is_active==True).all()
    return jobs


def update_job_by_id(job_id: int, job: JobCreate, session: Session,
                     owner_id: int) -> Job:
    existing_job = session.query(Job).filter(Job.id == job_id)
    if not existing_job.first():
        return None
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    session.commit()
    return existing_job.first()


def delete_job_by_id(job_id: int, session: Session):
    existing_job = session.query(Job).filter(Job.id == job_id)
    if not existing_job.first():
        return None
    existing_job.delete()
    session.commit()
    return True
