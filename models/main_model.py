from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from base.base_model import BaseModel
import json


class LSTMModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True,
                       input_shape=(self.config['input_shape'][0], self.config['input_shape'][1])))
        model.add(Dropout(0.2))
        model.add(LSTM(units=100, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=50))
        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def save_model(self, f="lstm_model.h5"):  # Updated file extension to .h5
        self.model.save(f)
