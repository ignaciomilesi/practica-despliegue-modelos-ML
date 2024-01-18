# creo las clase de entrada y salida que utilizara la app

from pydantic import BaseModel

class PredictionRequest(BaseModel):
    Species: str 
    Light_ISF: float
    Soil : str 
    Sterile : str 
    Conspecific : str 
    AMF : float
    EMF : float
    Phenolics : float
    Lignin : float
    NSC : float

class PredictionResponse(BaseModel):
    Event : float



# si quiero que un valor sea opcional   age: Optional[int] = None