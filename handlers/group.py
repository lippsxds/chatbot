from pyrogram import filters
from utils.ai_reply import get_ai_reply

def register_handlers(app):
    @app.on_message(filters.group & filters.text)
    async def group_text_handler(client, message):
        bot_username = (await client.get_me()).username
        if f"@{bot_username}" in message.text:
            user_id = message.from_user.id
            text = message.text.replace(f"@{bot_username}", "")
            reply_text, mood = await get_ai_reply(user_id, text)
            await message.reply_text(reply_text)
