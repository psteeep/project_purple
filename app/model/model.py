import tensorflow as tf


class ModelLoader:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, data):
        # Assuming data is in the same format as input to your LSTM model
        # You may need to preprocess the data accordingly
        predictions = self.model.predict(data)
        return predictions
