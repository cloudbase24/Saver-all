import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27199948"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "68e3e661a6e39a85abae162101855321")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chatfair2024:uLlpzegI2qYyGsnJ@chatfair.j0yxmxo.mongodb.net/?retryWrites=true&w=majority&appName=Chatfair")
