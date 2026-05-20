import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import uvicorn

app = FastAPI()


model = mlflow.pyfunc.load_model(
    "models:/LREG_Production_Model_VF_REG/Production"
)

print(f"Le model a ete charger la version  \n {model.metadata}")

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
@app.post("/")
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
        app,
        host="127.0.0.1",
        port = 8080
    )