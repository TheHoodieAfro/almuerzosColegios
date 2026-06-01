@router.post("/checkin")
def check_in(request: CheckInRequest):  # ← FastAPI reads the schema here
    # by the time you're inside this function, `request` is already
    # a validated Python object. No manual parsing needed.
    record = crud.create_record(student_id=request.student_id)
    return AttendanceResponse.from_orm(record)  # ← schema shapes the output
