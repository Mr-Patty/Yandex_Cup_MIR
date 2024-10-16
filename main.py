from models.train_module import TrainModule
from utils import initialize_logging, load_config

import argparse


# Создание парсера
parser = argparse.ArgumentParser(description="Пример программы с argparse")

# Добавление аргументов
parser.add_argument('--config', type=str, help='Возраст пользователя', default="./config/config_colab.yaml")
parser.add_argument('--log_config', type=str, help='Возраст пользователя', default="./config/logging_config.yaml")

args = parser.parse_args()

config = args.config
log_conf = args.log_config

config = load_config(config_path=config)
initialize_logging(config_path=log_conf, debug=False)
trainer = TrainModule(config)
trainer.pipeline()
trainer.test()
