from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from ..base_class_model import PredictiveModel

class LogisticRegressionModel(PredictiveModel):
    """ Logistic regression model for predicting personality. """

    def build_model(self) -> BaseEstimator:
        return LogisticRegression(
            solver='liblinear', 
            random_state=42,
            max_iter=1000,
            class_weight='balanced'
        )