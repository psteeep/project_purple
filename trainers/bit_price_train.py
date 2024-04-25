from base.base_train import BaseTrain


class LSTMTrain(BaseTrain):
    def train(self):
        self.model.compile(optimizer=self.config['optimizer'], loss=self.config['loss'], metrics=self.config['metrics'])
        history = self.model.fit(self.X_train, self.y_train, epochs=self.config['num_epochs'],
                                 batch_size=self.config['batch_size'], validation_split=self.config['validation_split'])
