# actualiza el modelo. Se copia lo analizado en el notebook
# se se busca la mejora solo el estimador GradientBoostingClassifier, 
# ya que incluir mas impactaria en el tiempo de actualizacion

import logging
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, cross_validate, train_test_split

import utils

utils.logging_basic_config()



logging.info("Cargando data...")

dataset = pd.read_csv("dataset/data_Modif.csv")
# dropeo, una ves mas, cualquier observacion con algun valor nulo
dataset =  dataset.dropna()


logging.info("Separando data...")

X = dataset.drop(['Event'], axis = 1)
y = dataset['Event']


logging.info("Generando modelo...")

num_cols = ['Light_ISF', 'AMF', 'EMF', 'Phenolics', 'Lignin', 'NSC']
cat_cols = ['Species', 'Soil', 'Sterile', 'Conspecific']

col_trans = ColumnTransformer([
    ('scalador_col_num', StandardScaler(), num_cols),
    ('one-hot_cat_num', OneHotEncoder(), cat_cols)
    ],
    remainder='drop')

estimador = Pipeline([
    ('manejo de columnas', col_trans),
    ('core_model', GradientBoostingClassifier())
])


logging.info("Buscando mejores hiperparametros...")

parametros = {
    'core_model__n_estimators': range(100,200,10),
    'core_model__max_depth' : range(2,11)
} 

rand_est = RandomizedSearchCV(
    estimador,
    parametros,
    n_iter= 10,
    cv=3,
    scoring="r2")
    
rand_est.fit(X, y)

mejorEstimador = rand_est.best_estimator_


logging.info("Validacion cruzada del mejor estimador...")

resultados = cross_validate(mejorEstimador, X, y, cv=10, return_train_score=True)

trainScore = np.mean(resultados['train_score'])
testScore = np.mean(resultados['test_score'])

logging.info(f'Mejor estimador Train Score: {round(trainScore, 6)}')
logging.info(f'Mejor estimador Test Score: {round(testScore, 6)}')


logging.info("Generando nuevo modelo y actualizando...")

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30)
mejorEstimador.fit(X_train, y_train)

utils.update_model(mejorEstimador)

logging.info("Generando reporte de modelo...")

validation_score = mejorEstimador.score(X_test, y_test)
utils.save_simple_metrics_report(trainScore, testScore, validation_score, mejorEstimador)

logging.info("Entrenamiento completado")

breakpoint()

