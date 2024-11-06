from app.database import Base, engine
from app.models import Invoice

Base.metadata.create_all(bind=engine)

print("Table created successfully")