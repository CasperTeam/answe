from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup

@Client.on_message(filters.command(["chemistry"]))
async def chemistry(bot, update):

       source = requests.get("https://teletype.in/@satyendra/Chemistry").text
       soup = BeautifulSoup(source, "lxml")
       text = "\n".join(_.text for _ in soup.find("article").find_all("p"))
       await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)
