import os
from typing import Union
from fastapi import FastAPI
from components import getContainerById, getContainers

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/containers")
def containers():
    # data = [i for i in getContainers()]7
    data = getContainers()
    return data
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}