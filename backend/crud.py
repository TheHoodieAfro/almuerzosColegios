from datetime import datetime, timezone
from pathlib import Path

import models
import pandas as pd
from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent.parent
STUDENTS_FILE = BASE_DIR / "data" / "Estudiantes.xlsx"


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

    now = datetime.now(timezone.utc)
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


def get_records_from_last_month(db: Session) -> list[models.AttendanceRecord]:
    now = datetime.now(timezone.utc)
    start = (now - relativedelta(months=1)).replace(
        day=1, hour=0, minute=0, second=0, microsecond=0
    )
    end = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    return (
        db.query(models.AttendanceRecord)
        .filter(
            models.AttendanceRecord.registro >= start,
            models.AttendanceRecord.registro < end,
        )
        .all()
    )
