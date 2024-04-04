import os

API_ID = API_ID = 28982573

API_HASH = os.environ.get("API_HASH", "aee939a0fddb972d443b8e98c383ea1f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7001564218:AAHgValTyIg1AxzEOilOYfNHD3r70djG4qY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6842796809))

LOG = -1002078377131

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6842796809").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


