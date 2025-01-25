import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_models(predictor, X_test, Y_test, parameters):

    results = {}
    best_models = {}  # Dictionary to store the best models

    prediction = predictor.predict(X_test)

    mae = mean_absolute_error(Y_test, prediction)
    mse = mean_squared_error(Y_test, prediction)
    r2 = r2_score(Y_test, prediction)

    result = {
        'MAE': mae,
        'MSE': mse,
        'R2': r2
    }

    print(f"  MAE: {mae:.2f}")
    print(f"  MSE: {mse:.2f}")
    print(f"  R2: {r2:.2f}")

    # Save the model for the current target column
    model_path = f"data/models/model.pkl"
    predictor.save(model_path)
    print(f"\nModel saved to {model_path}")

    # Create a DataFrame with evaluation metrics
    results_df = pd.DataFrame.from_dict(results, orient='index').reset_index()
    results_df.rename(columns={'index': 'Target'}, inplace=True)

    print("\nFinal Evaluation Results:\n")
    print(results_df)

    return results_df, predictor
