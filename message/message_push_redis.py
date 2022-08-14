# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from discordmonitor.monitorserverconfig import *
from message.template.message_obsever import *


class MessagePushRedis(object):
    def init(self, message_obsever: MessageObsever):
      self.message_obsever = message_obsever

    @logger.catch
    async def handle(self):
      logger.info(f"message_obsever={self.message_obsever}")
      redis = aioredis.from_url(monitorserverconfig_instance.get_auth_token())

      stream_field = self.message_obsever.name() + "|" + self.message_obsever.message_id
      stream_dict = {stream_field: self.message_obsever.get_serialize_data()}
      await redis.xadd("oceanmonitor_stream", stream_dict)
      logger.debug(f"message_push_redis_succ={self.message_obsever}")
