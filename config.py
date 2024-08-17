from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("20621590")
APP_HASH = os.environ.get("a7e91275d681fefd4b2453b158b254ec")
BOT_USERNAME = os.environ.get("Nshsuskkkkhsbot")
session = os.environ.get("1BJWap1wBuwkETHYij2BrnXC7oLYn7DTzpB8CdY3TNoqYuVXHR_8D9FhhJonvzadRDFb9m0fnt39HAvb7dPcX4jKSR5E8F-miqERcrm_bgu5VBIzkVf2ni0NR3Vc3JqFqY6J8JVxIyHCG1kLplqg3P6kFMcPYfIi6Xd8Q1jkuk43fDA8jz9lDOBlZZr12mPpqFfrCEVXNKaBLnHBT7rr59GT54Y0d-AiUOBjGaDTiv-FQESjlR-qSMMWAcQmgF6Z2mOlfN3PZWfPmKh0N8NXjvhvrvlmDHmHwlSSL1HypmdSm4L171HnEMoF2CWJRezyImGD-N2XRKBFDHE6pGNGQEatWI7Ylo-E=")
SESSION = os.environ.get("1BJWap1wBuwkETHYij2BrnXC7oLYn7DTzpB8CdY3TNoqYuVXHR_8D9FhhJonvzadRDFb9m0fnt39HAvb7dPcX4jKSR5E8F-miqERcrm_bgu5VBIzkVf2ni0NR3Vc3JqFqY6J8JVxIyHCG1kLplqg3P6kFMcPYfIi6Xd8Q1jkuk43fDA8jz9lDOBlZZr12mPpqFfrCEVXNKaBLnHBT7rr59GT54Y0d-AiUOBjGaDTiv-FQESjlR-qSMMWAcQmgF6Z2mOlfN3PZWfPmKh0N8NXjvhvrvlmDHmHwlSSL1HypmdSm4L171HnEMoF2CWJRezyImGD-N2XRKBFDHE6pGNGQEatWI7Ylo-E=")
token = os.environ.get("7495582036:AAFSFqyBILat1qCFIFD5f-18Zmm0huC2sMk")
sython = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

