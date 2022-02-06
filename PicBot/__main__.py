import os
import pyrogram
import logging
from PicBot.config_var import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="PicBot/Plugins")
    app = pyrogram.Client(
        "PicBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )

import logging
from tglogging import TelegramLogHandler

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="[SECURED!]",             log_chat_id=-1001543238877, 
            update_interval=2, 
            minimum_lines=1, 
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("name")

logger.info("live log streaming to telegram.")

    app.run()
