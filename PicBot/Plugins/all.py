from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup
from PicBot.config_var import Config

@Client.on_message(filters.command(["all"]))
async def all(bot, update):
        if update.from_user.id in Config.AUTH_USERS:
                source1 = requests.get("https://teletype.in/@satyendra/Maths").text
                i = BeautifulSoup(source1, "lxml")
                satya1 = "\n".join(_.text for _ in i.find("article").find_all("p"))
                source2 = requests.get("https://teletype.in/@satyendra/Chemistry").text
                i = BeautifulSoup(source2, "lxml")
                satya2 = "\n".join(_.text for _ in i.find("article").find_all("p"))
                source3 = requests.get("https://teletype.in/@satyendra/Physics").text
                i = BeautifulSoup(source3, "lxml")
                satya3 = "\n".join(_.text for _ in i.find("article").find_all("p"))
                text = (satya1+satya3+satya2)
                await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)
        else:
         text="**Wait A Min**\n**Who Are You**"
         await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)