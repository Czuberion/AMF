from kedro.pipeline import Pipeline, node

from .app.streamlit_run import streamlit_run
from .data.clean_data import clean_data
from .data.perform_analysis import perform_analysis
from .data.split_data import split_data
from .model.evaluate_models import evaluate_models
from .model.train_models import train_models


def create_pipeline(**kwargs):
    return Pipeline(
        [
            # Whole pipeline
            node(
                func=perform_analysis,
                inputs="food_time_raw",
                outputs="food_time_analyzed",
                name="perform_analysis_node",
            ),
            node(
                func=clean_data,
                inputs="food_time_analyzed",
                outputs="food_time_cleaned",
                name="clean_data_node",
            ),
            node(
                func=split_data,
                inputs=["food_time_cleaned", "parameters"],
                outputs=[
                    "X_train",
                    "X_dev",
                    "X_test",
                    "Y_train",
                    "Y_dev",
                    "Y_test"],
                name="split_data_node",
            ),
            node(
                func=train_models,
                inputs=["X_train", "Y_train", "X_dev", "Y_dev", "parameters"],
                outputs="trained_models",
                name="train_models_node",
            ),
            node(
                func=evaluate_models,
                inputs=["trained_models", "X_test", "Y_test", "parameters"],
                outputs=["model_metrics", "best_model"],
                name="evaluate_models_node",
            ),
            node(
                func=streamlit_run,
                inputs=["best_model"],
                outputs=None,
                name="streamlit_node",
            ),
            # # Only streamlit
            #     node(
            #         func=streamlit_run,
            #         inputs="dummy_input",
            #         outputs=None,
            #         name="streamlit_node"
            #     )
        ]
    )
