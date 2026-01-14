import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "Wine_quality.pkl")
model = joblib.load(MODEL_PATH)

def model_prediction(user_input: dict):
    df = pd.DataFrame([user_input])

    # Rename columns to match training data
    df.rename(columns={
        "fixed_acidity": "fixed acidity",
        "volatile_acidity": "volatile acidity",
        "citric_acid": "citric acid",
        "residual_sugar": "residual sugar",
        "chlorides": "chlorides",
        "free_sulfur_dioxide": "free sulfur dioxide",
        "total_sulfur_dioxide": "total sulfur dioxide",
        "density": "density",
        "pH": "pH",
        "sulphates": "sulphates",
        "alcohol": "alcohol"
    }, inplace=True)

    # ✅ Convert NumPy → Python
    predicted_class = int(model.predict(df)[0])

    probabilities = model.predict_proba(df)[0]
    confidence = float(max(probabilities))

    class_probs = {
        int(cls): float(round(prob, 4))
        for cls, prob in zip(model.classes_, probabilities)
    }

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probs
    }
