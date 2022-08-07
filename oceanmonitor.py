# coding=utf-8
from discordmonitor.discordmonitor import DiscordMonitor
from utils.oceanlogger import OceanLogger
from loguru import logger


class OceanMonitorServer:
    def __init__(self):
      # 初始化logger 配置
      OceanLogger()

    def start(self):
      DiscordMonitor().start()


if __name__ == "__main__":
    server = OceanMonitorServer()
    server.start()
