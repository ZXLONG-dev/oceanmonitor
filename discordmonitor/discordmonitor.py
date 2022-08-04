# coding=utf-8
import aiohttp
import asyncio
import json
from loguru import logger

from discordmonitor.channel_token import *
from discordmonitor.channelconfig import *

class DiscordMonitor:
    def __init__(self):
        logger.info("init discord monitor")
        self.keep_times = 1
        self.max_keep_times = 100

    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start_new_dc_connection(LONG_TOKEN, "LONG_TOKEN_NAME"))

    async def start_new_dc_connection(self, token: str, token_name: str):
        connect_times = 1
        while True:
            self.keep_times = 1
            logger.info(f"start_new_dc_connection {connect_times}")

            WS_URL = "wss://gateway.discord.gg/?encoding=json&v=9"
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as client:
                async with client.ws_connect(WS_URL, autoclose=False, max_msg_size=0) as ws:
                    await ws.send_str(get_dc_identify_info(token))

                    # 心跳保活
                    asyncio.create_task(self.keep_connection(token_name, ws))

                    # 处理消息
                    await self.dispatch(token, token_name, ws)
                    await asyncio.sleep(5)
                    connect_times += 1

    async def keep_connection(self, token_name: str, ws):
        await asyncio.sleep(10)
        while True:
            try:
                if self.keep_times >= self.max_keep_times:
                    raise Exception("max_keep_times")

                heartbeat = '''{"op":1,"d":%d}''' % self.keep_times
                logger.debug(f"{token_name} keep connection :{heartbeat}, keep_times: {self.keep_times}")
                await ws.send_str(heartbeat)
                await asyncio.sleep(41.25)
                self.keep_times += 1
            except Exception as e:
                logger.error(f"{token_name} keep connection error :{e}")
                await asyncio.sleep(5)
                await ws.close()
                return

    async def dispatch(self, token: str, token_name: str, ws):
        # 鉴权结果
        dc_response = await ws.receive()
        if dc_response.type != aiohttp.WSMsgType.TEXT or json.loads(dc_response.data).get('d') == None:
            logger.error(f"{dc_response}")
            return

        dc_response = await ws.receive()
        if dc_response.type != aiohttp.WSMsgType.TEXT or json.loads(dc_response.data).get('t') == None:
            logger.error(f"{dc_response}")
            return 

        while True:
            if self.keep_times >= self.max_keep_times:
                return

            dc_response = await ws.receive()
            if dc_response.type != aiohttp.WSMsgType.TEXT:
                logger.error(f"{dc_response} exception= {ws.exception()}")
                return 

            dc_response = json.loads(dc_response.data)
            if dc_response.get('t') != 'MESSAGE_CREATE':
                continue

            dc_response = dc_response['d']
            if channelconfig_instance.check_channelid(dc_response.get('channel_id')) == False:
                continue

            logger.debug(f'{dc_response}')
