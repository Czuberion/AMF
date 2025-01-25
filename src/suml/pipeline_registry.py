from kedro.pipeline import Pipeline
from suml.pipelines import pipeline as ds_pipeline

def register_pipelines():
    return {
        "ds": ds_pipeline.create_pipeline(),
        "__default__": ds_pipeline.create_pipeline(),
    }
