# coding=utf-8
import asyncio
from discordmonitor.discordmonitor import DiscordMonitor
from oceanwebsocket.oceanwebsocket import OceanWebSocketServer
from utils.oceanlogger import OceanLogger
from loguru import logger


class OceanMonitorServer:
    def __init__(self):
      # 初始化logger 配置
      OceanLogger()

    def start(self):
      DiscordMonitor().start()
      # OceanWebSocketServer().start()

      # await asyncio.gather(OceanWebSocketServer(self.loop).start())
      # await asyncio.gather(DiscordMonitor().start(), OceanWebSocketServer().start())

if __name__ == "__main__":
    server = OceanMonitorServer()
    server.start()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(OceanMonitorServer().start())

