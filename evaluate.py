def evaluate_model(tpot, X_test, y_test):
    accuracy = tpot.score(X_test, y_test)
    print(f"Test Accuracy: {accuracy:.4f}")
    return accuracy
