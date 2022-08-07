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
    
    def check_channelid(self, channel_id: str) -> bool:
        all_channel_id = self.get_test_channelid()
        return channel_id in all_channel_id

    def get_channeltoken(self, monitor_section: str) -> list:
        channel_token = []
        if self.server_config.has_section(monitor_section) == True:
            for key in self.server_config[monitor_section]:
                channel_token.append(self.server_config[monitor_section][key])

        return channel_token

    def get_test_channelid(self) -> list:
        return self.get_channeltoken("StaffTestChannel")


channelconfig_instance = CheckoutChannelConfig()
