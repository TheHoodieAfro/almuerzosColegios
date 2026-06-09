from db import Base
from sqlalchemy import Column, DateTime, Integer, String


class AttendanceRecord(Base):
    __tablename__ = "records"

    id = Column(String, primary_key=True)
    colegio_id = Column(String, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    registro = Column(DateTime, nullable=False)
