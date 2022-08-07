# coding=utf-8
from discordmonitor.discordmonitor import DiscordMonitor
from utils.oceanlogger import OceanLogger


class Server:
    def __init__(self):
      # 初始化logger 配置
      OceanLogger()

    def start(self):
      DiscordMonitor().start()


if __name__ == "__main__":
    Server().start()
