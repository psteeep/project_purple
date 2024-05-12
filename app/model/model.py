import pickle
from typing import List

__version__ = "0.1.0"

with open(f"trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


def predict(text: str) -> List[float]:
    return model.predict([text])
