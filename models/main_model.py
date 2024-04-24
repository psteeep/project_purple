from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from data_loader.data_retrieve import DataProcessor
import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import json

with open('../configs/config.json') as jf:
    cfg = json.load(jf)

# Initialize DataProcessor with the file path
data_processor = DataProcessor('C:/git/project_purple/data_loader/data sets/main.csv')

# Load the data
data = data_processor.load_data()

# Extract the closing prices
close = data['Close'].values.reshape(-1, 1)

# See the train data length
train_close_len = math.ceil(len(close) * 0.8)
print(train_close_len)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(close)

# Create the training dataset
train_data = scaled_data[0:train_close_len, :]
# Create X_train and y_train
X_train = []
y_train = []
for i in range(60, len(train_data)):
    X_train.append(train_data[i - 60:i, 0])
    y_train.append(train_data[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Create the testing dataset
test_data = scaled_data[train_close_len - 60:, :]
# Create X_test and y_test
X_test = []
y_test = data.iloc[train_close_len:, :]
for i in range(60, len(test_data)):
    X_test.append(test_data[i - 60:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Build the LSTM model
optimized_model = Sequential()
optimized_model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
optimized_model.add(Dropout(0.2))
optimized_model.add(LSTM(units=100, return_sequences=False))
optimized_model.add(Dropout(0.2))
optimized_model.add(Dense(units=50))
optimized_model.add(Dense(units=1))

# Compile the model
optimized_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model with fewer epochs
history = optimized_model.fit(X_train, y_train, epochs=cfg['num_epochs'], batch_size=cfg['batch_size'],
                              validation_split=0.1)

# Predict with LSTM model
predictions = optimized_model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# Plot the data
train = close[:train_close_len]
valid = pd.DataFrame(close[train_close_len:], columns=['Close'])  # Convert to DataFrame
valid["Predictions"] = predictions.flatten()  # Flatten predictions to match shape

# Visualize the data
plt.figure(figsize=(16, 8))
plt.title("LSTM Model")
plt.xlabel("Time", fontsize=14)
plt.ylabel("USDT", fontsize=14)
plt.plot(data["Close Time"][:train_close_len], train)
plt.plot(data["Close Time"][train_close_len:], valid[["Close", "Predictions"]])
plt.legend(["Train", "Validation", "Predictions"], loc="lower right")
plt.show()
