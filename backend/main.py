import pandas as pd
from fastapi import FastAPI

app = FastAPI()
data = pd.read_csv('data.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}