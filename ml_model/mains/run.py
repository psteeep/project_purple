import json
import matplotlib.pyplot as plt
from ml_model.data_loader.data_retrieve import DataProcessor
from ml_model.models.main_model import LSTMModel
from ml_model.trainers.bit_price_train import LSTMTrain
from sklearn.model_selection import train_test_split


def main():
    try:
        with open('../configs/config.json', 'r') as jf:
            cfg = json.load(jf)

        data_processor = DataProcessor('C:/git/project_purple/data_loader/data sets/main.csv')
        data = data_processor.load_data()
        scaled_data = data_processor.preprocess_data(data)
        X, y, scaler = data_processor.prepare_train_data(scaled_data)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        lstm_model = LSTMModel(cfg)
        lstm_train = LSTMTrain(lstm_model.model, X_train, y_train, cfg)
        lstm_train.train()

        lstm_model.save_model("lstm_model.h5")  # Updated file extension to .h5

        predictions = lstm_model.model.predict(X_test)
        predictions = scaler.inverse_transform(predictions)

        train_len = len(X_train)
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
