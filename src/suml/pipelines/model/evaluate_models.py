import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_models(predictor, x_test, y_test, parameters):

    # Predict
    prediction = predictor.predict(x_test)

    # Calculate metrics
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    r2 = r2_score(y_test, prediction)

    result = {"MAE": mae, "MSE": mse, "R2": r2}

    # Create a DataFrame with evaluation metrics
    results_df = pd.DataFrame.from_dict(result, orient="index").reset_index()
    results_df.rename(columns={"index": "Metric", 0: "Value"}, inplace=True)

    print("\nFinal Evaluation Results:\n")
    print(results_df)

    return results_df, predictor
