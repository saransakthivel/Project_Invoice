from pydantic import BaseModel
from typing import Optional

class InvoiceCreate(BaseModel):
    customer_name:str
    amount:float
    status:str

class Invoice(InvoiceCreate):
    id:int

    class Config:
        orm_mode = True

class InvoiceUpdate(BaseModel):
    customer_name :Optional[str]=None
    status : Optional[str]=None

    class config:
        orm_mode = True