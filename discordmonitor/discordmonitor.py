# coding=utf-8
import aiohttp
import asyncio
import json
from loguru import logger

from discordmonitor.channel_token import *


class DiscordMonitor:
    def __init__(self):
        logger.info("init discord monitor")

    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start_new_dc_connection(TOE_TOKEN, "TOE_TOKEN_NAME"))


    async def start_new_dc_connection(self, token: str, token_name: str, connect_times=0):
        logger.info("start_new_dc_connection")
        if connect_times >= 100:
            return f"connect {token_name} error"

        WS_URL = "wss://gateway.discord.gg/?encoding=json&v=9"
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as client:
            async with client.ws_connect(WS_URL, autoclose=False, max_msg_size=0) as ws:
                await ws.send_str(get_dc_identify_info(token))

                # 心跳保活
                asyncio.create_task(self.keep_connection(token, token_name, connect_times, ws))

                # 处理消息
                await self.dispatch(token, token_name, ws)

    async def keep_connection(self, token: str, token_name: str, connect_times, ws):
        await asyncio.sleep(10)
        keep_times = 1
        while True:
            try:
                heartbeat = '''{"op":1,"d":%d}''' % keep_times
                logger.debug(f"{token_name} keep connection :{heartbeat}")
                await ws.send_str(heartbeat)
                await asyncio.sleep(41.25)
                keep_times += 1
            except Exception as e:
                await asyncio.sleep(5)
                await ws.close()
                asyncio.create_task(self.start_new_dc_connection(
                    token, token_name, connect_times+1))

    async def dispatch(self, token: str, token_name: str, ws):
        while True:
            dc_response = await ws.receive()
            logger.debug(f"{dc_response}")

            dc_response = json.loads(dc_response.data).get('d', False)
            logger.debug(f"{dc_response}")

            dc_response = await ws.receive()
            if dc_response.type == aiohttp.WSMsgType.TEXT:
                dc_response = json.loads(dc_response.data).get('t', False)
                logger.debug(f"{dc_response}")

            dc_response = await ws.receive()
            if dc_response.type == aiohttp.WSMsgType.TEXT:
                dc_response = json.loads(dc_response.data)
                logger.debug(f"{dc_response}")
