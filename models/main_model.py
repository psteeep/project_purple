from keras.layers import LSTM, Dense
from keras.models import Sequential
from data_loader.data_retrieve import DataRetrieve
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

model = Sequential()

data = DataRetrieve('C:/git/project_purple/data_loader/data sets/BTC-Daily.csv')
dataset = data.data_load()

X = dataset[['open', 'high', 'low', 'Volume BTC']].values
y = dataset['close'].values

scaler = MinMaxScaler(feature_range=(0, 1))
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32)


predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)

print(predictions)
