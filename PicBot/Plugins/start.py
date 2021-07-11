from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types.update import Update


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
     await bot.reply_text("You are not authorized") 
     return
    text=f"__Hello!__\nI'm answersbot\nCheck /help to get available commands"
    mypic="https://telegra.ph/file/72fc24c9fff47f87ed937.jpg"
    await bot.send_photo(
            update.chat.id,
            mypic,
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("website", url="https://teletype.in/@satyendra/Answers")],[InlineKeyboardButton("Contact Me", url="https://t.me/a_L_Satya")]]
            ),
        )
