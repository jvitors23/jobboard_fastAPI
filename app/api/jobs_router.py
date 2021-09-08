from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db_session
from schemas.jobs import JobCreate, JobResponse
from db.crud.jobs import create_new_job


router = APIRouter()


@router.post('/create-job', response_model=JobResponse)
def create_job(job: JobCreate, session: Session = Depends(get_db_session)):
    """Job creation endpoint"""
    owner_id = 1
    job = create_new_job(job=job, session=session, owner_id=owner_id)
    return job
