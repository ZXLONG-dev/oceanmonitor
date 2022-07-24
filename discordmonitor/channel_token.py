# coding=utf-8

TOE_TOKEN = 'NTkxMTAwNjM0NjE5NDQ1MjQ4.X0O6SQ.eVvdexctXenLKXYb_EZeJ7OCsRY'  # harry.z


def get_dc_identify_info(token: str) -> str:
  auth_info = '''
      {"op":2,"d":{"token":"%s","capabilities":125,"properties":{"os":"Windows","browser":"Chrome","device":"","system_locale":"zh-CN","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36","browser_version":"91.0.4472.106","os_version":"10","referrer":"https://discord.com/channels/671183199912853504/819676110010187826","referring_domain":"discord.com","referrer_current":"https://discord.com/channels/671183199912853504/819676110010187826","referring_domain_current":"discord.com","release_channel":"stable","client_build_number":87781,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1}}}
  ''' % token

  return auth_info
