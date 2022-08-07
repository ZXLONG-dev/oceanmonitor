# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from discordmonitor.monitorserverconfig import *


class MessagePushRedis(object):
    def init(self, listener: object):
      self.listener = listener

    @logger.catch
    async def handle(self):
      redis = aioredis.from_url(monitorserverconfig_instance.get_auth_token())
      stream_dict = {self.listener.message_id: self.listener.get_serialize_data()}
      await redis.xadd("oceanmonitor_stream", stream_dict)
      logger.debug(f"message_push_redis_succ={self.listener}")
