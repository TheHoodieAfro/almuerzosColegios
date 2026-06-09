from datetime import datetime, timezone

import models
from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import Session


def create_record(db: Session, colegio_id: str) -> models.AttendanceRecord:

    now = datetime.now(timezone.utc)

    record_id = f"{colegio_id}_{now.strftime('%Y%m%d%H%M%S')}"
    nombres = "test"
    apellidos = "test"

    record = models.AttendanceRecord(
        id=record_id,
        colegio_id=colegio_id,
        nombres=nombres,
        apellidos=apellidos,
        tiempo=datetime.now(timezone.utc),
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
            models.AttendanceRecord.tiempo >= start,
            models.AttendanceRecord.tiempo < end,
        )
        .all()
    )
