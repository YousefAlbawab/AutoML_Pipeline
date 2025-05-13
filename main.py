from data_processing import load_data, split_data
from automl_pipeline import train_automl
from evaluate import evaluate_model

# Load and split data
X, y = load_data()
X_train, X_test, y_train, y_test = split_data(X, y)

# Train AutoML pipeline
tpot = train_automl(X_train, y_train)

# Evaluate model
evaluate_model(tpot, X_test, y_test)

# Export best pipeline
tpot.export('best_model.py')
