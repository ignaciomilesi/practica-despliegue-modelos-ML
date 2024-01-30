from sklearn.pipeline import Pipeline
from joblib import dump

import logging

def logging_basic_config() -> None:
    # esto es un registro para el manejo de info, errores, etc
    logging.basicConfig(
        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
        level= logging.INFO,
        datefmt= '%H:%M:%S' 
    )


def update_model(model : Pipeline) -> None:
    dump(model, 'model/model.pkl')

def save_simple_metrics_report(train_score: float, test_score: float, validation_score: float, model: Pipeline) -> None:
    with open("report.txt", "w") as report_file:
        report_file.write("# Reporte del pipeline del modelo "+"\n")

        for key, value in model.named_steps.items():
            report_file.write(f"### {key}:{value.__repr__()}"+"\n")

        report_file.write(f'### Train Score: {train_score}'+'\n')
        report_file.write(f'### Test Score: {test_score}'+'\n')
        report_file.write(f'### Validation Score: {validation_score}'+'\n')