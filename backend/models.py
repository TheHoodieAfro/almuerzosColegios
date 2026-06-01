from db import Base
from sqlalchemy import Column, DateTime, Integer, String


class AttendanceRecord(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String)
    student_name = Column(String)
    timestamp = Column(DateTime)
