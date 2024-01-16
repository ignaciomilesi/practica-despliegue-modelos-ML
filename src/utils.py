import logging

def logging_basic_config() -> None:
    # esto es un registro para el manejo de info, errores, etc
    logging.basicConfig(
        format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
        level= logging.INFO,
        datefmt= '%H:%M:%S' 
    )

