from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud
from ..models import Invoice as InvoiceModel
from ..schemas import InvoiceUpdate


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

@router.get("/invoices/{id}")
def get_invoice(id: int, db:Session=Depends(get_db)):
    return crud.get_invoice_by_id(db=db, id=id)

@router.put("/invoices/{invoice_id}", response_model=schemas.InvoiceUpdate)
def update_invoice(invoice_id: int, invoice_update: InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = db.query(InvoiceModel).filter(InvoiceModel.id == invoice_id).first()

    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    update_data = invoice_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_invoice, key, value)

@router.delete("/invoices/{id}", response_model=dict)
def delete_invoice(id: int, db: Session = Depends(get_db)):
    db_invoice=db.query(InvoiceModel).filter(InvoiceModel.id == id).first()

    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    db.delete(db_invoice)
    db.commit()
    
    return {'msg': 'Invoice Deleted Succesfully'}
