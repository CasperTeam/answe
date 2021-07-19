from pyrogram import Client, filters
from PicBot.config_var import Config

@Client.on_message(filters.command(["help"]))
async def help_menu(bot, update):
     if update.from_user.id in Config.AUTH_USERS:
      text = f"**Hey theese are the available commands:**\n"
      text += f"➤ /start - To start Me:)\n"
      text += f"➤ /help - To get this message\n"
      text += f"➤ /physics - sends physics answers from website\n"
      text += f"➤ /chemistry - sends chemistry answers from website\n"
      text += f"➤ /maths - sends maths answers from website\n"
      text += f"➤ /all - main command to get all answers in single message"
      await bot.send_message(update.chat.id, text=text)
     else:
        text="**Wait A Min**\n**Who Are You**"
        await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)
