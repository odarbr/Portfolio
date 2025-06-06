from abc import ABC, abstractmethod
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score

class PredictiveModel(ABC):

    """ Abstract class for predictive models. """

    def __init__(self):
        pass

    @abstractmethod
    def build_model(self):
        """ Construct and return model. """
        pass

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """ Train the model using the provided features and labels. """
        self.model = self.build_model()
        self.model.fit(X, y)

    def predict(self, X: pd.DataFrame) -> pd.Series:
        """ Predict the personality labels for the given features. """
        return self.model.predict(X)
    
    def evaluate(self, X: pd.DataFrame, y_true: pd.Series) -> float:
        """ Evaluate the model using accuracy as metric. """
        y_pred = self.predict(X)
        return accuracy_score(y_true, y_pred)
    
    def get_model(self):
        return self.model