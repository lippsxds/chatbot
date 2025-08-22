from pyrogram import filters
from config import OWNER_ID
from utils.broadcast import broadcast_text

def register_handlers(app):
    @app.on_message(filters.private & filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast_command(client, message):
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await message.reply_text("Usage: /broadcast Your message here")
            return
        await broadcast_text(client, message, text[1])

