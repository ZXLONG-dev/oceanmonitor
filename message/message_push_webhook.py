# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from discordmonitor.monitorserverconfig import *


class MessagePushWebhook(object):
    def init(self, listener: object):
      self.listener = listener

    async def handle(self):
      return None
