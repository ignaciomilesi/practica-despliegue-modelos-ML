# actualiza el modelo. Se copia lo analizado en el notebook
# pero se utiliza LogisticRegression en ves de GradientBoostingClassifier por el tiempo de ejecucion

import logging
import warnings
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_validate, train_test_split

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
    ('core_model', LogisticRegression())
])


logging.info("Buscando mejores hiperparametros...")

parametros = {
    'core_model__solver': ['lbfgs', 'liblinear'],
    'core_model__penalty': ['l1', 'l2', None],
    'core_model__C': [0.001, 0.01, 0.1, 1.0],
    'core_model__max_iter' : [100, 500, 1000]
} 

gridSearc = GridSearchCV(
    estimador,
    parametros,
    cv=3,
    scoring="r2")
    
warnings.filterwarnings('ignore')
# para ignorar las advertencias y no ensuciar la salida, 
# ya que avisa que hay convinacciones que no las tomara encuenta por no ser validas

gridSearc.fit(X, y)
warnings.filterwarnings('default') #vuelvo a dejar que se vena las advertencias

mejorEstimador = gridSearc.best_estimator_


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
