# creo las clase de entrada y salida que utilizara la app

from pydantic import BaseModel
from pydantic import validator

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

    @validator('Species')
    def categoria_especies(cls, especie):

        especiesAdmitidas = ['Acer saccharum', 'Quercus alba', 'Quercus rubra', 'Prunus serotina']

        if not (especie in especiesAdmitidas):
            raise ValueError('Especie no admitida. Las especies admitidas son: ' + str(especiesAdmitidas))
        
        return especie
    

    @validator('Soil')
    def categoria_suelo(cls, suelo):

        sueloAdmitido = ['Prunus serotina', 'Quercus rubra', 'Acer rubrum', 
                         'Populus grandidentata', 'Sterile', 'Acer saccharum', 'Quercus alba']

        if not (suelo in sueloAdmitido):
            raise ValueError('Suelo no admitido. Los suelos admitidos son: ' + str(sueloAdmitido))
        
        return suelo
    
    @validator('Sterile')
    def categoria_esteril(cls, esteril):

        esterilAdmitido = ['Non-Sterile', 'Sterile']

        if not (esteril in esterilAdmitido):
            raise ValueError('Esteril no admitido. Los valores admitidos son: ' + str(esterilAdmitido))
        
        return esteril
    
    @validator('Conspecific')
    def categoria_conespecificida(cls, conespecificidad):

        conespecificidadAdmitida = ['Heterospecific', 'Sterilized', 'Conspecific']

        if not (conespecificidad in conespecificidadAdmitida):
            raise ValueError('Conespecificidad no admitida. Los valores admitidos son: ' + str(conespecificidadAdmitida))
        
        return conespecificidad

        

class PredictionResponse(BaseModel):
    Event : float



def categoria_especies(cls, valor, valoresAdmitidos):

    if not (valor in valoresAdmitidos):
        raise ValueError('Valor no admitido. Los valores admitidas son: ' + str(valoresAdmitidos))
        
    return valor


# si quiero que un valor sea opcional   age: Optional[int] = None