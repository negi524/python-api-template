from logging import Logger
import yaml
import logging
import logging.config
from pathlib import Path

log_setting_file_path: str = (
    f"{Path(__file__).resolve().parent.parent}/config/logsetting.yml"
)

# ログ設定読み込み
with open(log_setting_file_path, "r") as file:
    logging.config.dictConfig(yaml.safe_load(file))


def get_logger(logger_name: str) -> Logger:
    """loggerを取得する

    Args:
        logger_name (str): loggerの名称

    Returns:
        Logger: logger
    """
    logger = logging.getLogger(logger_name)
    return logger
