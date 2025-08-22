from pyrogram import filters
from pyrogram.types import Message

def register_handlers(app):
    @app.on_message(filters.private & (filters.sticker | filters.video | filters.photo))
    async def media_handler(client, message: Message):
        if message.sticker:
            await message.reply_sticker(message.sticker.file_id)
        elif message.photo:
            await message.reply_photo(message.photo.file_id)
        elif message.video:
            await message.reply_video(message.video.file_id)

