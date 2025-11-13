from .BaseModel import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, Text

class Venue(Base):
    __tablename__ = "venue"

    venueId = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255))
    address = mapped_column(Text)
    city = mapped_column(String(100))
    capacity = mapped_column(Integer)
