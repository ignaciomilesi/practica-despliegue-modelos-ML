# Practica de despliegue de modelos de Machine Learning
---

## Introduccion
---
En este repositorio se encuentra el código necesario para desplegar un modelo de Machine Learning. Se busca detallar el paso a paso para poder realizar el despliegue y conocer el flujo de MLOps.

Se analizan las técnicas empleadas con el fin de implementar y automatizar la integración continua (CI), la entrega continua (CD) y el entrenamiento continuo (CT) para sistemas de aprendizaje automático (AA).

Diseñar y entrenar un modelo de AA es solo una pequeña parte del desafio, lo verdaderamente complejo es su implementacion, que comprende la configuración, automatización, recopilación y  verificación de datos, pruebas y depuración, la administración de recursos, el análisis de modelos, la administración de metadatos y procesos, la infraestructura de entregas y la supervisión. Es por ello que comienza a plicarse las practicas de MLops.

MLOps es una práctica de la ingeniería de AA, cuyo fin es unificar el desarrollo (Dev) y las operaciones (Ops) del sistema de AA. La práctica de MLOps implica abogar por la automatización y la supervisión en todos los pasos de la construcción del sistema de AA, incluida la integración, las pruebas, el lanzamiento, la implementación y la administración de la infraestructura.

## Arquitectura del proyecto
---
![Arquitectura](img/Arquitectura.png)

- Se codificara en Python y se usara la biblioteca scikit-learn para la generacion de modelos
- Se utiliza GitHub coomo gestor de versiones del codigo y DVC como gestor de versiones del dataset y de los modelos
- Como servicio de alojamiento del modelo y dataset se utilizara Google drive
- Se utiliza GitHub Action para el proceso de integración continua y despliegue continuo (CI / CD)
- Por ultimo se utiliza FastAPI para la creacion del API REST y Docker para el despliegue del servicio

Por medio de Github actions, se van a activar tres workflows diferentes:

- Testing: se va a encargar de ejecutar los test unitarios

- CI / CD: se va a encargar de la creacion del docker y desplegar el servicio cada ves que hay una actualizacion del modelo.

- Reentrenamiento: va a utilizar Scikit learn para reentrenar un modelo de Machine Learning y generar nuevos modelos actualizados.

## Distribucion de archivos
---