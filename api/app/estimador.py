from .model import PredictionRequest
from .utils import get_model, transform_to_dataframe

# cargo el modelo
model = get_model()

def getPrediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return prediction