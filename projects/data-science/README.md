# Personality Prediction Data Science Project

This folder contains a small example project that predicts personality traits from survey data.

## Contents
- `src/data` - sample dataset in CSV format
- `src/data_normalization` - utilities for preparing the dataset
- `src/predictive_models` - simple machine learning models
- `src/run_predictive_models.py` - command line entry point
- `src/notebooks` - Jupyter notebook with exploratory analysis

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