# Bitcoin Time Series Prediction

This project aims to predict financial time series using LSTM neural networks. It includes functionalities to preprocess data, train LSTM models, and serve predictions via a FastAPI web service.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/psteeep/project_purple.git
    ```

## Docker

You can also run the project using Docker. First, build the Docker image:

```bash
docker build -t bitcoin-prediction .
```
than run
```
docker run -p 8000:8000 financial-prediction
```

## Data Format

The training data is structured in the following format:

| Open Time   | Open      | High      | Low       | Close     | Volume    | Close Time | Quote Asset Volume | Number of Trades | Taker buy base asset volume | Taker buy quote asset volume |
|-------------|-----------|-----------|-----------|-----------|-----------|------------|---------------------|------------------|-----------------------------|------------------------------|
| 1.60946E+12 | 28923.63  | 28961.66  | 28913.12  | 28961.66  | 27.457032 | 1.60946E+12 | 794382.044          | 1292             | 16.777195                   | 485390.8268                  |
| 1.60946E+12 | 28961.67  | 29017.5   | 28961.01  | 29009.91  | 58.477501 | 1.60946E+12 | 1695802.897         | 1651             | 33.733818                   | 978176.4682                  |

## Input Data

The model accepts input in the following format:

```json
{
  "close_time": [
    "1609459259999",
    "1609459319999"
  ],
  "close_prices": [
    28961.66,
    29009.91
  ]
}
```

## Model Output

The model returns predicted prices for the provided input data:

```json
{
  "train_data": {
    "close_time": [
      "1609459259999",
      "1609459319999"
    ],
    "close_prices": [
      28961.66,
      29009.91
    ]
  },
  "validation_data": {
    "close_time": [
      "1609459259999",
      "1609459319999"
    ],
    "close_prices": [
      28961.66,
      29009.91
    ]
  },
  "predicted_prices": [
    1.5202429294586182,
    1.5202429294586182
  ]
}
```
