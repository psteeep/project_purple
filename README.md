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
