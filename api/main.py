import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware
import sentry_sdk

sentry_sdk.init(
    # Remplacez par votre propre DSN Sentry
    dsn="your_sentry_dsn_here",
    send_default_pii=True,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL_PATH)

print("True")

class Student_input(BaseModel):
    age: int
    sex: int          
    Medu: int
    Fedu: int
    studytime: int
    failures: int
    absences: int
    goout: int
    Walc: int         
    health: int
    higher: int       
    internet: int     
    traveltime: int
    freetime: int
    famrel: int

@app.get("/")
async def root():
    return {"message": "API FastAPI fonctionne"}


@app.post("/predict")
async def predection_endpoint(data: Student_input):
    
     data_input = data.dict()
     
     data_frame = pd.DataFrame([data_input])
     
     prediction = model.predict(data_frame)
     
     return {"The result is " : int(prediction[0])}

if __name__ ==  '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port = 7860
    )