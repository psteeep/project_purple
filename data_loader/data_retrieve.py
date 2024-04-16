import pandas as pd 

class DataRetrieve():

    def __init__(self, file_path) -> None:
        self.data = None
        self.file_path = file_path

    def data_load(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

    def process_data(self):
        missing_values = self.data.isnull().sum()
        without_missing = self.data.dropna()
        return self.data.fillna(self.data.mean())

    def get_data(self, criteria = None):
        pass

    def filtre_data(self, criteria):
        pass

    def update_data(self, new_data):
        pass
