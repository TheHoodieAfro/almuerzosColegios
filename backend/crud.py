from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import os
import models
import pandas as pd
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
STUDENTS_FILE = DATA_DIR / "JORNADA UNICA -SEDE BACHILLERATO.xlsx"

BOGOTA_TZ = ZoneInfo("America/Bogota")


def get_student_from_excel(documento: str) -> dict | None:
    df = pd.read_excel(STUDENTS_FILE)
    student = df[df["Documento"] == str(documento)]

    if student.empty:
        return None

    return {
        "nombres": student.iloc[0]["Apellidos y nombre del estudiante"],
        "grado": student.iloc[0]["Grado"],
        "grupo": student.iloc[0]["Grupo"],
    }


def create_record(db: Session, documento: str) -> models.AttendanceRecord | None:

    now = datetime.now(BOGOTA_TZ)
    record_id = f"{documento}_{now.strftime('%Y%m%d%H%M%S')}"

    student = get_student_from_excel(documento)
    if student is None:
        return None

    record = models.AttendanceRecord(
        id=record_id,
        documento=documento,
        nombres=student["nombres"],
        grado=str(student["grado"]),
        grupo=student["grupo"],
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
