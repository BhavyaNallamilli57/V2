# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "16978078"))
API_HASH = getenv("API_HASH", "91ccaf748f031b656bbf64ff47f990e3")
BOT_TOKEN = getenv("BOT_TOKEN", "8047715996:AAFVsIkVIUu2SdxIo5ywNmVUhQqImm4Gjlo")
OWNER_ID = list(map(int, getenv("OWNER_ID", "854075907").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saverestrict:saverestrict@cluster0.cqgezzb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1004858441331")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001533796760"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "urlshortx.com")
AD_API = getenv("AD_API", "72ac8c94409d87e12b5357265192b637769ae67f")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
