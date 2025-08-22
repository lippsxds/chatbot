from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import private, group, media, owner

app = Client("ai_gf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

private.register_handlers(app)
group.register_handlers(app)
media.register_handlers(app)
owner.register_handlers(app)

print("🤖 AI Girlfriend Bot is running...")
app.run()
