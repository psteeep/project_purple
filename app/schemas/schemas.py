from pydantic import BaseModel


class PriceIn(BaseModel):
    price: int


class PredictionOut(BaseModel):
    pred_price: int
