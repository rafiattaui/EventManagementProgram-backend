from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String
from BaseModel import Base

class Customer(Base):
    __tablename__ = "customer"

    customerId = mapped_column(Integer, primary_key=True)
    firstName = mapped_column(String(100))
    lastName = mapped_column(String(100))
    email = mapped_column(String(255), unique=True)
    password = mapped_column(String(255))
    phoneNumber = mapped_column(String(20), unique=True)