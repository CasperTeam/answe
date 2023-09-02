import os

import heroku3

from dotenv import load_dotenv
from distutils.util import strtobool

if os.path.exists("local.env"):
    load_dotenv("local.env")

def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")
    
class Config(object):
    API_ID = 2171111
    API_HASH = "fd7acd07303760c52dcc0ed8b2f73086"
    BOT_TOKEN = "5067445854:"
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    ADMIN = ("1089528685 1560627554 1761119103 752115419 2096436923 1743515951 1590779595 1450446335 1781750526  1360207635 404752610 995222609 1068690405 1892645791 1780233082 1808004347 1907558615 1651439896 1008863370 1485347648")
    AUTH_USERS = [int(admin) for admin in (ADMIN).split()]
