from .BaseModel import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String


class Organizer(Base):
    __tablename__ = "organizer"

    organizerId = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    email = mapped_column(String(255))
    contactNum = mapped_column(String(20), unique=True)
    website = mapped_column(String(100))
