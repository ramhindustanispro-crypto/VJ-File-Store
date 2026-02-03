# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "31839535"))
API_HASH = environ.get("API_HASH", "0cdb557873264c3925a65c332e96e854")
BOT_TOKEN = environ.get("BOT_TOKEN", "8532071762:AAFQmgnQ6cDaGOmJw_e4iu58TOQ2YkYxE6k")

PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1414257528').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "motionprimebot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Information
DB_URI = environ.get("DB_URI", "https://motion-prime-default-rtdb.firebaseio.com/")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "720")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "4320")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003863255661"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', True)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "https://linkpays.in/api?") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "aeaee53f2af867d5bd1c7232de78add78b5f4dd9") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/c/3295359958/11") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', True)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://motionprimr.blogspot.com/2026/02/motion-prime.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://intelligent-angela-motionprime-b9551ad0.koyeb.app/")


# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
