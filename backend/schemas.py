from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, field_serializer


class AttendanceResponse(BaseModel):
    documento: str
    nombres: str
    grado: str
    grupo: str
    registro: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("registro")
    def format_registro(self, value: datetime) -> str:
        return value.strftime("%d/%m/%Y %H:%M")  # → "09/06/2026 03:54"


class CheckInRequest(BaseModel):
    documento: str


class ReportResponse(BaseModel):
    start: date
    end: date
    total: int
    records: list[AttendanceResponse]
