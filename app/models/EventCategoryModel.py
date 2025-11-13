from .BaseModel import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

class EventCategory(Base):
    __tablename__ = "eventcategory"

    eventCategoryId = mapped_column(Integer, primary_key=True)
    category = mapped_column(String(25))