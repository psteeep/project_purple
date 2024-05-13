from fastapi import APIRouter
from ..model.model import ModelLoader
from ..schemas.schemas import PredictionData, PredictionResponse
import logging

import numpy as np


def preprocess_data(close_time, close_prices):
    # Convert close_time to integers
    close_time = [int(time) for time in close_time]

    # Combine close_time and close_prices into sequences
    sequences = list(zip(close_time, close_prices))

    # Convert sequences to numpy array
    sequences_array = np.array(sequences)

    return sequences_array


router = APIRouter()

# Initialize the model loader with the path to your saved LSTM model
model_loader = ModelLoader("mains/lstm_model.h5")

logger = logging.getLogger(__name__)
@router.post("/predict", response_model=PredictionResponse)
def predict_route(data: PredictionData):
    try:
        # Preprocess the data before passing it to the model
        sequences = preprocess_data(data.close_time, data.close_prices)

        # Make predictions using the loaded model
        predictions = model_loader.predict(sequences)

        # Convert predictions to list of floats
        predictions = [float(pred) for pred in predictions]

        # Log predictions for debugging
        logger.debug("Predictions: %s", predictions)

        # Form the response
        response = PredictionResponse(
            train_data=data,
            validation_data=data,
            predicted_prices=predictions
        )

        return response

    except Exception as e:
        # Log any exceptions that occur during prediction
        logger.exception("An error occurred during prediction: %s", str(e))
        raise
