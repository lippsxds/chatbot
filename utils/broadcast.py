from pyrogram import Client
from config import OWNER_ID

async def broadcast_text(client: Client, message, text: str):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ You are not the owner!")
        return

    async for dialog in client.get_dialogs():
        try:
            await client.send_message(dialog.chat.id, text)
        except:
            pass
    await message.reply_text("✅ Broadcast completed!")

