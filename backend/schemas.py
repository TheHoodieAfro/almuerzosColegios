from datetime import datetime

from pydantic import BaseModel


# What the API receives when a student checks in
class CheckInRequest(BaseModel):
    colegio_id: str


# What the API sends back after a check-in
class AttendanceResponse(BaseModel):
    id: str
    colegio_id: str
    nombres: str
    apellidos: str
    registro: datetime

    class Config:
        from_attributes = True  # allows converting a DB model directly to this schema
