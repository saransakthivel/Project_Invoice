from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {'msg' : 'This is home page'}

@app.get('/about')
def about():
    return {'about':'Company details'}

@app.get('/user/{id},{name}')
def user(id : int, name : str, height : Optional[float] = None):
    return {"data" : {"id": id, "name": name, "height" : height}}

 