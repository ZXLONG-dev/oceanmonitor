# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from discordmonitor.monitorserverconfig import *
from message.message_push_redis import * 
from message.message_push_webhook import *

class MessageHandle(object):
    def init(self, listener: object):
      self.listener = listener

    async def flow(self):
      loop = asyncio.get_event_loop()

      task1 = MessagePushRedis()
      task1.init(self.listener)
      async_task1 = loop.create_task(task1.handle())

      task2 = MessagePushWebhook()
      task2.init(self.listener)
      async_task2 = loop.create_task(task2.handle())

      await asyncio.gather(async_task1, async_task2)