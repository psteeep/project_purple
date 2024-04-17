import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, file_path):
        self.data = None
        self.file_path = file_path

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

    def miss_data(self):
        numeric_columns = self.data.select_dtypes(include='number').columns
        self.data[numeric_columns] = self.data[numeric_columns].fillna(self.data[numeric_columns].mean())
        return self.data

    def process_data(self):
        self.data = self.miss_data()  # Handle missing values
        scaler = MinMaxScaler(feature_range=(0, 1))
        self.data[['open', 'high', 'low', 'Volume BTC']] = scaler.fit_transform(self.data[['open', 'high', 'low', 'Volume BTC']])
        self.data['close'] = scaler.fit_transform(self.data['close'].values.reshape(-1, 1))
        return self.data

    def split_data(self, test_size=0.2, random_state=42):
        X = self.data[['open', 'high', 'low', 'Volume BTC']].values
        y = self.data['close'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test
