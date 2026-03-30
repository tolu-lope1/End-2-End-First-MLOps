from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
from config import model_path, scaler_path

app = FastAPI()
scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

class DiabetesInput(BaseModel):
    Pregnancies : int
    Glucose: float
    BloodPressure: float
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live"}


@app.post("/single-predict")
def predict(data: DiabetesInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, 
                            data.SkinThickness, data.Insulin, data.BMI, 
                            data.DiabetesPedigreeFunction, data.Age]])
    
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]
    print(prediction)
    return {"diabetic": bool(prediction)}

@app.post("/multi-predict")
def predict(data: List[DiabetesInput]):
    input_data = np.array([list(d.dict().values()) for d in data])
    scaled_data = scaler.transform(input_data)
    predictions = model.predict(scaled_data)
    data_predictions = [bool(p) for p in predictions]
    return {"predictions": data_predictions}
