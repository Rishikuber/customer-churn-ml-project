from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("customer_churn_model.pkl")

# Define expected input structure
class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float
    CustomerSupportCalls: int
    LatePayments: int
    DataUsageGB: float
    AvgSessionMinutes: float
    SatisfactionScore: int


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}


@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)[0]

    if prediction == 1:
        return {"prediction": "Customer likely to churn"}
    else:
        return {"prediction": "Customer likely to stay"}