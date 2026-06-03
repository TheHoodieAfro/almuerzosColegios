import crud
from db import get_db
from fastapi import APIRouter, Depends
from schemas import AttendanceResponse, CheckInRequest
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/checkin")
def check_in(request: CheckInRequest, db: Session = Depends(get_db)):

    record = crud.create_record(db, request.student_id)
    return AttendanceResponse.from_orm(record)
