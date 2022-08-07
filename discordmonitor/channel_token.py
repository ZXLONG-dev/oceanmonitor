# coding=utf-8

LONG_TOKEN = 'ODI1OTA5NDE3ODEwOTg0OTgw.GVdNe-.1SE-UdN7EsJCyQZATNqneyQx1h5S9Va4htheho'  # long

def get_dc_identify_info(token: str) -> str:
  auth_info = '''
  {
    "op": 2,
    "d": {
      "token": "%s",
      "capabilities": 509,
      "properties": {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "zh-CN",
        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        "browser_version": "101.0.0.0",
        "os_version": "10",
        "referrer": "https://www.google.com/",
        "referring_domain": "www.google.com",
        "search_engine": "google",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 139460,
        "client_event_source": null
      },
      "presence": {
        "status": "online",
        "since": 0,
        "activities": [],
        "afk": false
      },
      "compress": false,
      "client_state": {
        "guild_hashes": {},
        "highest_last_message_id": "0",
        "read_state_version": 0,
        "user_guild_settings_version": -1,
        "user_settings_version": -1
      }
    }
  }
  ''' % token

  return auth_info
