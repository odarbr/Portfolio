# Personality Prediction Data Science Project

This folder contains a small example project that predicts personality traits from survey data.

## Project Structure

```
projects/data-science/src
├── data/
├── notebooks/
├── predictive_models/               
│   ├── base_class_model.py
│   ├── logistic_regression_model.py
│   └── decision_tree_model.py
├── run_predictive_model.py
```

### Contents
- `/data` - sample dataset in CSV format
- `/data_normalization` - utilities for preparing the dataset
- `/predictive_models` - simple machine learning models
- `/run_predictive_models.py` - command line entry point
- `/notebooks` - Jupyter notebook with exploratory analysis

## Dataset
The dataset includes features like:
- Time spent alone
- Stage fear (Yes/No)
- Social event attendance
- Going outside
- Drained after socializing (Yes/No)
- Friends circle size
- Post frequency on social media

The target label is: `Personality` (Introvert or Extrovert).

## Quick start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run one of the predictive models:
   ```bash
   python src/run_predictive_models.py -m logreg -d src/data/personality_dataset.csv
   ```
   Use `-m tree` to run the decision tree model instead.

The script splits the dataset, trains the selected model, and prints the accuracy on a test set.
Both predictive models produce an accuracy of around 0.93.

Feel free to explore, modify, or expand the project!