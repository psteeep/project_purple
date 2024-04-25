from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import json

class LSTMModel(BaseModel):
    def build_model(self):
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(self.config['input_shape'], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=100, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=50))
        model.add(Dense(units=1))
        return model

    def save_model(self, file_path):
        self.model.save(file_path)
