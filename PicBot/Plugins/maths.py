from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup

@Client.on_message(filters.command(["maths"]))
async def maths(bot, update):
     source = requests.get('https://teletype.in/@satyendra/Maths').text
     soup = BeautifulSoup(source, 'lxml')
     text = soup.article.text
     await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)