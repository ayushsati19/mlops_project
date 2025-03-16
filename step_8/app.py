# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib  # For loading the saved model
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Step 1: Load the best model
MODEL_PATH = "Gradient_Boosting_best_model.pkl"  # Replace with the actual path to your saved model
try:
    model = joblib.load(MODEL_PATH)  # Load the model using joblib
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")

# Step 2: Define the input schema for the API
class InputData(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

# Step 3: Create the prediction endpoint
@app.post("/predict")
async def predict(input_data: InputData):
    try:
        # Convert input data to a dictionary and then to a DataFrame
        input_dict = input_data.dict()
        input_df = pd.DataFrame([input_dict])

        # Rename columns to match the preprocessing pipeline's expectations
        input_df.rename(columns={
            "education_num": "education-num",
            "marital_status": "marital-status",
            "capital_gain": "capital-gain",
            "capital_loss": "capital-loss",
            "hours_per_week": "hours-per-week",
            "native_country": "native-country"
        }, inplace=True)

        # Make predictions using the loaded model
        prediction = model.predict(input_df)[0]

        # Map the prediction to a human-readable label
        prediction_label = " >50K" if prediction == 1 else " <=50K"

        # Return the prediction as JSON
        return {"prediction": prediction_label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")

# Step 4: Add a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}