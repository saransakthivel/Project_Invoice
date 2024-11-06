from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key = True, index = True)
    customer_name = Column(String(255), index=True)
    amount = Column(Float)
    status = Column(String(100))