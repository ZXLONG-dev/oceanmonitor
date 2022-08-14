import configparser
from utils.singleton import *
import os

@singleton
class CheckoutChannelConfig(object):
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        etc_file_path = os.path.join(path, 'etc/channelconfig.ini')
        self.server_config = configparser.ConfigParser()
        self.server_config.read(etc_file_path)

    def get_sectioon(self, monitor_section: str) -> list:
        item = []
        if self.server_config.has_section(monitor_section) == True:
            for key in self.server_config[monitor_section]:
                item.append(self.server_config[monitor_section][key])
        return item

    def check_channelid(self, channel_id: str) -> bool:
        all_channel_id = self.get_test_channelid()
        return channel_id in all_channel_id

    def get_test_channelid(self) -> list:
        return self.get_sectioon("StaffTestChannel")

    def get_push_webhook_list(self) -> list:
        return self.get_sectioon("PUSHWEBHOOK")


channelconfig_instance = CheckoutChannelConfig()
