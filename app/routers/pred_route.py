from fastapi import APIRouter
from ..model.model import predict
from ..schemas.schemas import PredictionData, PredictionResponse

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict_route(text: str):
    # Get predictions using the model
    result = predict(text)

    # For demonstration, I'm returning dummy data for the train and validation data
    dummy_train_data = PredictionData(close_time=["2024-01-01", "2024-01-02"], close_prices=[100, 101])
    dummy_validation_data = PredictionData(close_time=["2024-01-03", "2024-01-04"], close_prices=[102, 103])

    # Form the response using the predicted result and dummy data
    response = PredictionResponse(
        train_data=dummy_train_data,
        validation_data=dummy_validation_data,
        predicted_prices=result
    )

    return response
