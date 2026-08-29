from db import Base
from sqlalchemy import Column, DateTime, String


class AttendanceRecord(Base):
    __tablename__ = "records"

    id = Column(String, primary_key=True)
    documento = Column(String, nullable=False)
    nombres = Column(String, nullable=False)
    grado = Column(String, nullable=False)
    grupo = Column(String, nullable=False)
    registro = Column(DateTime, nullable=False)
