import pandas as pd
from autogluon.tabular import TabularPredictor
import os

def train_models(X_train, Y_train, X_dev, Y_dev, parameters):

    print("Parameters received:", parameters)

    if 'autogluon' not in parameters or 'model_path' not in parameters['autogluon']:
        raise ValueError("The 'model_path' key is missing in the 'autogluon' section of parameters.")

    model_path = parameters['autogluon']['model_path']

    # Zmieniamy sposób wypisania celu, zamiast wypisywać całego Y_train, wypisujemy nazwę kolumny
    print(f"\nTraining AutoGluon for target: TARGET")

    # Łączenie X_train i Y_train w jeden DataFrame
    train_data = pd.concat([X_train, Y_train], axis=1)
    dev_data = pd.concat([X_dev, Y_dev], axis=1)
    

    # Sprawdzanie typu train_data
    print(f'X_train type: {type(train_data)}')

    # Definiowanie metryki i typu problemu (domyślnie "regression")
    eval_metric = parameters['autogluon'].get('eval_metric', 'mean_absolute_error')

    save_path = 'data/models'

    # Trening modelu
    predictor = TabularPredictor(
        label='TARGET',  # Ustawiamy nazwę kolumny, nie całą serię
        eval_metric=eval_metric,
        path=save_path,
        problem_type='regression'  # Określamy typ problemu na regresję
    ).fit(
        train_data=train_data,
        time_limit=parameters['autogluon'].get('time_limit', 3600)
    )

    # Ocena wydajności modelu na danych walidacyjnych
    performance = predictor.evaluate(dev_data)
    print(f"Performance for TARGET: {performance}")

    return predictor
