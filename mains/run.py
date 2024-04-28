import json
import matplotlib.pyplot as plt
import pandas as pd
from data_loader.data_retrieve import DataProcessor
from models.main_model import LSTMModel
from trainers.bit_price_train import LSTMTrain


def main():
    try:
        with open('../configs/config.json') as jf:
            cfg = json.load(jf)

        data_processor = DataProcessor('C:/git/project_purple/data_loader/data sets/main.csv')
        data = data_processor.load_data()
        scaled_data = data_processor.preprocess_data(data)
        X_train, y_train = data_processor.prepare_train_data(scaled_data)

        # Initialize model
        lstm_model = LSTMModel(cfg)
        lstm_train = LSTMTrain(lstm_model.model, X_train, y_train)

        # Train the model
        lstm_train.train()

        # Save the model
        model_file_path = 'lstm_model.pkl'
        lstm_model.save_model(model_file_path)

        predictions = lstm_model.model.predict(X_test)
        predictions = scaler.inverse_transform(predictions)

        train = close[:train_close_len]
        valid = pd.DataFrame(close[train_close_len:], columns=['Close'])  # Convert to DataFrame
        valid["Predictions"] = predictions.flatten()  # Flatten predictions to match shape
    except Exception as e:
        print("Error: ", e)
    # Visualize the data
    plt.figure(figsize=(16, 8))
    plt.title("LSTM Model")
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("USDT", fontsize=14)
    plt.plot(data["Close Time"][:train_close_len], train)
    plt.plot(data["Close Time"][train_close_len:], valid[["Close", "Predictions"]])
    plt.legend(["Train", "Validation", "Predictions"], loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()