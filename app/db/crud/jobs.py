from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, session: Session, owner_id: int) -> Job:
    job = Job(**job.dict(), owner_id=owner_id)
    session.add(job)
    session.commit()
    session.refresh(job)
    return job
