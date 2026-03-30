import os
import joblib
from config import *
import pandas as pd

import os
import pandas as pd
import joblib


def test(test_path, model_path, scaler_path):

    # Check test dataset
    if not os.path.exists(test_path):
        print("Test Failed: Test dataset not found")
        return

    test_data = pd.read_csv(test_path)
    X_test = test_data[features]

    # Check model and scaler
    if os.path.exists(model_path) and os.path.exists(scaler_path):

        print("Test Passed: Model and Scaler files found")

        scaler = joblib.load(scaler_path)
        model = joblib.load(model_path)

        print("Model Loaded Successfully")
        print(f"Model Type: {type(model)}")

        # Scale test data
        scaled_data = scaler.transform(X_test)

        # Make predictions
        predictions = model.predict(scaled_data)

        print("Predictions:")
        print(predictions)

    else:
        print("Test Failed: Model or Scaler file not found")