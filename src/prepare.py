# crea un archivo: data_Modif.csv, a partir del dataset original 
# que solo contenga las columnas utiles para la generacion del modelo
 
import logging
import pandas as pd
from dvc import api
from io import StringIO


import utils

utils.logging_basic_config()



logging.info("Cargando data...")

dataset_path = api.read("dataset/Tree_Data.csv", remote="myremote", encoding="utf8")
dataset = pd.read_csv(StringIO(dataset_path))


logging.info("Ajustando valores...")

# elijo las columnas que me intera
dataset_modif = dataset[['Species', 'Light_ISF', 'Soil', 'Sterile', 
                         'Conspecific', 'AMF', 'EMF', 'Phenolics', 'Lignin', 'NSC', 'Event']]

# se reemplaza los valores Nan de EMF
dataset_modif.fillna(value={"EMF": 0}, inplace=True)

# elimino cualquier registro que poseea algun dato Nan
dataset_modif = dataset_modif.dropna()

dataset_modif.to_csv("dataset/data_Modif.csv", index=False)

logging.info("Data extraida y preparada")

