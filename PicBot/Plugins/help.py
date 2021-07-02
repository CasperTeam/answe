from pyrogram import Client, filters

@Client.on_message(filters.command(["help"]))
async def help_menu(bot, update):
     text = f"**Hey theese are the available commands:**\n"
     text += f"➤ /start - To start Me:)\n"
     text += f"➤ /help - To get this message\n"
     text += f"➤ /physics - sends physics answers from website\n"
     text += f"➤ /chemistry - sends chemistry answers from website\n"
     text += f"➤ /maths - sends maths answers from website"
     await bot.send_message(update.chat.id, text=text)
