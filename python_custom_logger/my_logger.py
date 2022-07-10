import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
import os

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)  # have to call it at least once to print info/debug level messages
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class CustomLogger:
    def __init__(self):
        pass

    def create(
        self, app_name: str = __name__, log_folder: str = "", log_prefix: str = "log_"
    ):
        log_file_name = "".join([log_prefix, datetime.now().isoformat()[:10], ".log"])
        if log_folder != "" and not os.path.exists(log_folder):
            os.makedirs(log_folder)
        
        log_file = os.path.join("Log", log_file_name)
        return self.get_logger(app_name, log_file)

    def get_logger(
        self,
        app_name: str,
        file_name: str,
        NEED_BACKUP_FILE: bool = True,
        NEED_SCREEN_AND_FILE: bool = True,
        level: int = logging.DEBUG,
        formatter: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        max_bytes: int = 10 * 1024 * 1024,
        backup_count: int = 10,
        encoding: str = "utf-8",
    ):
        self.logger = logging.getLogger(name=app_name)
        # self.logger.propagate = False
        self.logger.setLevel(level=level)

        logger_formatter = logging.Formatter(formatter)
        
        f_handler = (
            RotatingFileHandler(
                filename=file_name,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding=encoding
            )
            if NEED_BACKUP_FILE
            else logging.FileHandler(filename=file_name, encoding=encoding)
        )
        
        f_handler.setFormatter(logger_formatter)
        logger.addHandler(f_handler)

        # if NEED_SCREEN_AND_FILE:
        #     stream_handler = logging.StreamHandler()
        #     stream_handler.setFormatter(logger_formatter)
        #     self.logger.addHandler(stream_handler)

        return self.logger

