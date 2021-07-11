from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup

@Client.on_message(filters.command(["all"]))
async def all(bot, update):
        source1 = requests.get("https://teletype.in/@satyendra/Maths").text
        i = BeautifulSoup(source1, "lxml")
        satya1 = "\n".join(_.text for _ in i.find("article").find_all("p"))
        source2 = requests.get("https://teletype.in/@satyendra/Chemistry").text
        i = BeautifulSoup(source2, "lxml")
        satya2 = "\n".join(_.text for _ in i.find("article").find_all("p"))
        source3 = requests.get("https://teletype.in/@satyendra/Physics").text
        i = BeautifulSoup(source3, "lxml")
        satya3 = "\n".join(_.text for _ in i.find("article").find_all("p"))
        await bot.send_message(update.chat.id, satya1,satya2,satya3, reply_to_message_id=update.message_id)