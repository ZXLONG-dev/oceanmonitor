import configparser
from discordmonitor.singleton import *
import os


@singleton
class MonitorServerConfig(object):
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        etc_file_path = os.path.join(path, 'etc/monitorserver.ini')
        self.server_config = configparser.ConfigParser()
        self.server_config.read(etc_file_path)

    def get_config_item(self, monitor_section: str, item_key: str):
      if self.server_config.has_section(monitor_section) == True:
          return self.server_config[monitor_section][item_key]
      return None

    def get_auth_token(self) -> str:
        return self.get_config_item("Redis", "auth_token")


monitorserverconfig_instance = MonitorServerConfig()
