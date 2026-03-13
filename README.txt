# Customer Churn Prediction API

This project predicts customer churn using a machine learning model deployed as a FastAPI service.

## Features
- Machine learning model using Random Forest
- REST API built with FastAPI
- Real-time churn prediction
- Swagger documentation

## Run the API

pip install -r requirements.txt

python -m uvicorn Api.api:app --reload

## Test API

Open:
http://127.0.0.1:8000/docs