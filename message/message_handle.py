# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from discordmonitor.monitorserverconfig import *
from message.message_push_redis import *
from message.message_push_webhook import *
from loguru import logger
from message.template.message_obsever import *


class MessageHandle(object):
    def init(self, message_obsever: MessageObsever):
      self.message_obsever = message_obsever

    async def flow(self):

      task1 = MessagePushRedis()
      task1.init(self.message_obsever)
      asyncio.create_task(task1.handle())

      task2 = MessagePushWebhook()
      task2.init(self.message_obsever)
      asyncio.create_task(task2.handle())
