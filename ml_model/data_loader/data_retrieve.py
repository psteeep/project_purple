from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd


class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data

    def preprocess_data(self, data):
        close = data['Close'].values.reshape(-1, 1)
        self.scaler = MinMaxScaler()
        scaled_data = self.scaler.fit_transform(close)
        return scaled_data

    def prepare_train_data(self, scaled_data):
        X_train = []
        y_train = []
        for i in range(60, len(scaled_data)):
            X_train.append(scaled_data[i - 60:i, 0])
            y_train.append(scaled_data[i, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        return X_train, y_train, self.scaler
