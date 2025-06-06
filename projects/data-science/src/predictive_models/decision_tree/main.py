from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeClassifier
from ..base_class_model import PredictiveModel

class DecisionTreeModel(PredictiveModel):
    """ Decision tree model for predicting personality. """

    def build_model(self) -> BaseEstimator:
        # Decision trees handle both numerical and categorical data.
        return DecisionTreeClassifier(
            criterion='entropy',
            max_depth=5,
            random_state=42,
            class_weight='balanced'
        )