from db import Base
from sqlalchemy import Column, DateTime, Integer, String


class AttendanceRecord(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    colegio_id = Column(String, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    tiempo = Column(DateTime, nullable=False)
