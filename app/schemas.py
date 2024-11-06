from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    customer_name:str
    amount:float
    status:str

class Invoice(InvoiceCreate):
    id:int

    class Config:
        orm_mode=True