from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import models
import pandas as pd
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
STUDENTS_FILE = BASE_DIR / "data" / "Estudiantes.xlsx"

BOGOTA_TZ = ZoneInfo("America/Bogota")


def get_student_from_excel(student_id: str) -> dict | None:
    df = pd.read_excel(STUDENTS_FILE)
    student = df[df["colegio_id"] == int(student_id)]

    if student.empty:
        return None

    return {
        "name": student.iloc[0]["nombres"],
        "last_name": student.iloc[0]["apellidos"],
    }


def create_record(db: Session, colegio_id: str) -> models.AttendanceRecord | None:

    now = datetime.now(BOGOTA_TZ)
    record_id = f"{colegio_id}_{now.strftime('%Y%m%d%H%M%S')}"

    student = get_student_from_excel(colegio_id)
    if student is None:
        return None

    record = models.AttendanceRecord(
        id=record_id,
        colegio_id=colegio_id,
        nombres=student["name"],
        apellidos=student["last_name"],
        registro=now,
    )

    db.add(record)
    db.commit()

    return record


def get_records_by_range(
    db: Session, start: date, end: date
) -> list[models.AttendanceRecord]:

    start_dt = datetime(start.year, start.month, start.day, 0, 0, 0)
    end_dt = datetime(end.year, end.month, end.day, 23, 59, 59)

    return (
        db.query(models.AttendanceRecord)
        .filter(
            models.AttendanceRecord.registro >= start_dt,
            models.AttendanceRecord.registro <= end_dt,
        )
        .all()
    )
