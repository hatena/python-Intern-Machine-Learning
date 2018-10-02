from intern_ml.data import Data, Feature, Label
from typing import List


class Perceptron:
    def __init__(self, n_dimension: int) -> None:
        pass


    def score(self, features: List[Feature]) -> float:
        return 0.0


    def predict(self, features: List[Feature]) -> Label:
        if self.score(features) > 0:
            return Label.POSITIVE
        else:
            return Label.NEGATIVE


    def train(self, dataset: List[Data]) -> None:
        pass
