from fastapi import FastAPI
from .app.model import PredictionRequest, PredictionResponse
from .app.estimador import getPrediction

# creo la app
app = FastAPI(docs_url="/")

# creo la solicitud post para obtener una predicion en la direccion...  
@app.post("/v1/predic")
def make_model_predic(request : PredictionRequest):
    return PredictionResponse(Event = getPrediction(request))