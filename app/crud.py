from sqlalchemy.orm import session
from . import models, schemas

def create_invoice(db:session, invoice:schemas.InvoiceCreate):
    db_invoice = models.Invoice(**invoice.model_dump())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoice(db:session,skip:int=0,limit:int=10):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

def get_invoice_by_id(db:session, id:int):
    return db.query(models.Invoice).filter(models.Invoice.id == id).first()