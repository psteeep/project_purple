import json
import matplotlib.pyplot as plt
from data_loader.data_retrieve import DataProcessor
from models.main_model import LSTMModel
from trainers.bit_price_train import LSTMTrain
from sklearn.model_selection import train_test_split


def main():
    try:
        with open('../configs/config.json', 'r') as jf:
            cfg = json.load(jf)

        data_processor = DataProcessor('C:/git/project_purple/data_loader/data sets/main.csv')
        data = data_processor.load_data()
        scaled_data = data_processor.preprocess_data(data)
        X, y, scaler = data_processor.prepare_train_data(scaled_data)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        lstm_model = LSTMModel(cfg)
        lstm_train = LSTMTrain(lstm_model.model, X_train, y_train, cfg)
        lstm_train.train()

        # Predicting the test set
        predictions = lstm_model.model.predict(X_test)
        predictions = scaler.inverse_transform(predictions)

        # Plotting part assumes you're plotting test predictions with corresponding times
        train_len = len(X_train)  # Adjust index if you're plotting on full dataset
        actual = scaler.inverse_transform(y_test.reshape(-1, 1))

        plt.figure(figsize=(16, 8))
        plt.title("LSTM Model Predictions")
        plt.xlabel("Time", fontsize=14)
        plt.ylabel("USDT", fontsize=14)
        plt.plot(actual, label='Actual')
        plt.plot(predictions, label='Predicted')
        plt.legend(loc="lower right")
        plt.show()

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
