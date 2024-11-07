from fastapi import FastAPI
from .routers import invoice

app = FastAPI()

app.include_router(invoice.router)