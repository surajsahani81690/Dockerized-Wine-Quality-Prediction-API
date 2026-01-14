from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.model_prediction import model_prediction
app = FastAPI()

@app.get("/")
def home():
    return {'message' : "Wine Quality prediction Model"}

@app.post("/predict")
def predict_quality(data: UserInput):
    user_input = data.dict()
    try:
        prediction = model_prediction(user_input)
        return JSONResponse(status_code = 200, content = {"prediction": prediction})
    except Exception as e:
        return JSONResponse(status_code = 500, content = str(e))
