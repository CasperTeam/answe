from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text=f"__Hello!__\nI'm answersbot\nCheck /help to get available commands"
    mypic="https://telegra.ph/file/72fc24c9fff47f87ed937.jpg"
    await bot.send_photo(
            update.chat.id,
            mypic,
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("website", url="https://teletype.in/@satyendra/Answers")]]
                [[InlineKeyboardButton("contact mr", url="https://t.me/a_L_Satya")]]
            ),
        )
