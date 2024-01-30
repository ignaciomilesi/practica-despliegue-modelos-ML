from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os 
from io import BytesIO

def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH','model/model.pkl')
    with open(model_path, "rb") as fh:
        model = load(BytesIO(fh.read()))
    return model

def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.model_dump().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame