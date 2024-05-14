import abc

class BaseModel(abc.ABC):
    def __init__(self, config):
        self.config = config
        self.model = self.build_model()

    @abc.abstractmethod
    def build_model(self):
        pass

    @abc.abstractmethod
    def save_model(self, f="my_model.h5"):
        pass
