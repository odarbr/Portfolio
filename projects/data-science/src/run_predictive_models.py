import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from predictive_models.logistic_regression import LogisticRegressionModel
from predictive_models.decision_tree import DecisionTreeModel
from data_normalization import data_normalization

def setup_args():
    parser = argparse.ArgumentParser(description="Run predictive models")
    parser.add_argument("-m", "--model", type=str, choices=["logreg", "tree"], required=True, help="Model type: logreg or tree")
    parser.add_argument("-d", "--dataset", type=str, required=True, help="Path to the dataset")
    return parser.parse_args()

def load_data(path):
    df = data_normalization(path)
    X = df.drop("Personality", axis=1)
    y = df["Personality"]

    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "__main__":
    args = setup_args()

    X_train, X_test, y_train, y_test = load_data(args.dataset)

    if args.model == "logreg":
        model = LogisticRegressionModel()
    
    elif args.model == "tree":
        model = DecisionTreeModel()

    model.fit(X_train, y_train)
    accuracy = model.evaluate(X_test, y_test)
    print(f"\nFinal accuracy: {accuracy: .4f}")