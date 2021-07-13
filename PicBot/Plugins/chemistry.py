from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup
from PicBot.config_var import Config

@Client.on_message(filters.command(["chemistry"]))
async def chemistry(bot, update):
       if update.from_user.id in Config.AUTH_USERS:
              source = requests.get("https://teletype.in/@satyendra/Chemistry").text
              soup = BeautifulSoup(source, "lxml")
              text = "\n".join(_.text for _ in soup.find("article").find_all("p"))
              await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)
       else:
        text="**Wait A Min**\n**Who Are You**"
        await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)