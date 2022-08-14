# coding=utf-8
from loguru import logger
import asyncio
from discordmonitor.monitorserverconfig import *
from discordmonitor.channelconfig import *
import requests
from message.template.message_obsever import *


class MessagePushWebhook(object):
    def init(self, message_obsever: MessageObsever):
      self.message_obsever = message_obsever

    @logger.catch
    async def handle(self):
      for webhook_link in channelconfig_instance.get_push_webhook_list():
        asyncio.create_task(self.push_webhook(webhook_link))

    @logger.catch
    async def push_webhook(self, webhook_link: str):
      push_header = {"Content-Type": "application/json"}

      push = requests.post(webhook_link, headers=push_header, data=self.message_obsever.get_serialize_data())
      logger.debug(f"push_webhook={push}")
