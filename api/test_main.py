from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_prediccion_positiva():
    response = client.post('/v1/predic',
                           json={
                               "Species": "Acer saccharum",
                                "Light_ISF": 0.106,
                                "Soil": "Prunus serotina",
                                "Sterile": "Non-Sterile",
                                "Conspecific": "Heterospecific",
                                "AMF": 22.0,
                                "EMF": 0.0,
                                "Phenolics": -0.56,
                                "Lignin": 13.86,
                                "NSC": 12.15
                            })
    
    assert response.status_code == 200
    assert response.json()['Event'] == 1.0

def test_prediccion_negativa():
    response = client.post('/v1/predic',	
                           json={
                               "Species": "Quercus alba",
                                "Light_ISF": 0.106,
                                "Soil": "Populus grandidentata",
                                "Sterile": "Non-Sterile",
                                "Conspecific": "Heterospecific",
                                "AMF": 33.06,
                                "EMF": 43.79,
                                "Phenolics": 5.35,
                                "Lignin": 19.53,
                                "NSC": 22.14
                            })
    
    assert response.status_code == 200
    assert response.json()['Event'] == 0.0