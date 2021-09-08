from db.crud.jobs import create_new_job, retrieve_job
from db.session import get_db_session
from fastapi import APIRouter, Depends, HTTPException, status, Path
from schemas.jobs import JobCreate, JobResponse
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/create-job', response_model=JobResponse,
             status_code=status.HTTP_201_CREATED,
             response_description='Job created successfully!')
def create_job(job: JobCreate, session: Session = Depends(get_db_session)):
    """Job creation endpoint"""
    owner_id = 1
    job = create_new_job(job=job, session=session, owner_id=owner_id)
    return job


@router.get('/{job_id}', response_model=JobResponse,
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_404_NOT_FOUND: {'description': 'Job not found!'},
            })
def get_job(job_id: int = Path(..., title='The id of the job', ge=1),
            session: Session = Depends(get_db_session)):
    """Job retrieve endpoint"""
    job = retrieve_job(job_id=job_id, session=session)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
