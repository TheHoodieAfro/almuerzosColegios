import crud
from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import AttendanceResponse, CheckInRequest
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/checkin")
def check_in(request: CheckInRequest, db: Session = Depends(get_db)):

    record = crud.create_record(db, request.colegio_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Student not found in Excel file")
    return AttendanceResponse.model_validate(record)
