# coding=utf-8
from loguru import logger
from discordmonitor.singleton import *


@singleton
class MessageFactory(object):
    def __init__(self):
      self.obsever_list = {}

    def add_observer(self, unique_key: str, msg_observer: object):
      self.obsever_list.update({unique_key: msg_observer})

    def get_message_instance(self, msg_source: dict):
      if msg_source.get('channel_id') == None:
        logger.error(f"dict get channel_id error {msg_source}")
        return None
      if msg_source.get('web_site_name') == None:
        logger.error(f"dict get web_site_name error {msg_source}")
        return None

      unique_key = msg_source.get('web_site_name') + msg_source.get('channel_id')
      logger.info(f"unique_key={unique_key}")

      message_obsever = self.obsever_list.get(unique_key)
      message_obsever.init(msg_source)

      logger.info(f"message_obsever={message_obsever}")
      return message_obsever


messagefactory_instance = MessageFactory()
