from typing import List
from pydantic import BaseModel

class PredictionData(BaseModel):
    close_time: List[str]
    close_prices: List[float]

class PredictionResponse(BaseModel):
    train_data: PredictionData
    validation_data: PredictionData
    predicted_prices: List[float]
