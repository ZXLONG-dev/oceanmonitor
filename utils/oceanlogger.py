# coding=utf-8
import os
from loguru import logger

class OceanLogger(object):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, 'log/monitor.log')

        logger.add(
            file_path,
            encoding='utf-8',
            level="INFO",
            rotation="00:00",
            backtrace=True,
            diagnose=True)

        logger.add(
            file_path,
            encoding='utf-8',
            level='ERROR',
            rotation="00:00",
            backtrace=True,
            diagnose=True)
