
from pyrogram import filters
from pyrogram.types import Message
from utils.ai_reply import get_ai_reply, generate_voice, get_mood_sticker

def register_handlers(app):
    @app.on_message(filters.private & ~filters.command(["start", "broadcast"]))
    async def private_text_handler(client, message: Message):
        user_id = message.from_user.id
        text = message.text

        reply_text, mood = await get_ai_reply(user_id, text)

        await message.reply_text(reply_text)

        sticker_id = get_mood_sticker(mood)
        if sticker_id:
            await message.reply_sticker(sticker_id)

        voice = await generate_voice(reply_text)
        await message.reply_voice(voice)
