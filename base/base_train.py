import abc

class BaseTrain(abc.ABC):
    def __init__(self, model, X_train, y_train):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train

    @abc.abstractmethod
    def train(self):
        pass
