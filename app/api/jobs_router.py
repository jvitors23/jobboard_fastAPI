from db.crud.jobs import create_new_job, retrieve_job, retrieve_all_jobs, \
    update_job_by_id, delete_job_by_id
from db.session import get_db_session
from fastapi import APIRouter, Depends, HTTPException, status, Path
from schemas.jobs import JobCreate, JobResponse
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.post('/create', response_model=JobResponse,
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


@router.get('', response_model=List[JobResponse],
            status_code=status.HTTP_200_OK)
def get_jobs(session: Session = Depends(get_db_session)):
    """Job retrieve endpoint"""
    jobs = retrieve_all_jobs(session=session)
    return jobs


@router.put('/{job_id}/update',
            status_code=status.HTTP_200_OK, response_model=JobResponse)
def update_job(job: JobCreate,
               job_id: int = Path(..., title='The id of the job', ge=1),
               session: Session = Depends(get_db_session)):
    """Job update endpoint"""
    owner_id = 1
    job = update_job_by_id(job_id=job_id, job=job, session=session, owner_id=owner_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Job with id {job_id} does not exist')
    return job


@router.delete('/{job_id}/delete', status_code=status.HTTP_200_OK)
def delete_job(job_id: int = Path(..., title='The id of the job', ge=1),
               session: Session = Depends(get_db_session)):
    """Job update endpoint"""
    job = delete_job_by_id(job_id=job_id, session=session)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Job with id {job_id} does not exist')
    return {'detail': 'Successfully deleted!'}
