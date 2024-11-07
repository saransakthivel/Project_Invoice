from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/invoices/",response_model=schemas.Invoice)
def create_invoice(invoice:schemas.InvoiceCreate, db:Session = Depends(get_db)):
    return crud.create_invoice(db=db, invoice=invoice)

@router.get("/invoices/")
def read_invoice(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    invoices = crud.get_invoice(db=db, skip=skip, limit=limit)
    return invoices