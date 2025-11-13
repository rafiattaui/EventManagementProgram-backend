from .BaseModel import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Date, Time

class EventDateTime(Base):
    __tablename__ = "eventdatetime"

    eventDateTimeID = mapped_column(Integer, primary_key=True)
    date = mapped_column(Date)
    startTime = mapped_column(Time)
    endTime = mapped_column(Time)