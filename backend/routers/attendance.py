from datetime import date

import crud
from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import (
    AttendanceResponse,
    CheckInRequest,
    ReportResponse,
)
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/checkin")
def check_in(request: CheckInRequest, db: Session = Depends(get_db)):

    record = crud.create_record(db, request.colegio_id)
    if record is None:
        raise HTTPException(
            status_code=404, detail="Codigo incorrecto o estudiante no existente"
        )
    return AttendanceResponse.model_validate(record)


@router.get("/records")
def get_records(
    start: date, end: date, db: Session = Depends(get_db)
) -> ReportResponse:
    records = crud.get_records_by_range(db, start, end)
    return ReportResponse(
        start=start,
        end=end,
        total=len(records),
        records=[AttendanceResponse.model_validate(r) for r in records],
    )
