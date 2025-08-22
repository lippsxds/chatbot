import openai
from config import OPENAI_API_KEY
from utils.moods import get_user_mood, set_user_mood
from gtts import gTTS
from io import BytesIO

openai.api_key = OPENAI_API_KEY

MOOD_STICKERS = {
    "happy": "CAACAgUAAxkBAAEBH1Ng2Z9XY_happy_sticker",
    "sad": "CAACAgUAAxkBAAEBH2Ng2Z9XY_sad_sticker",
    "angry": "CAACAgUAAxkBAAEBH3Ng2Z9XY_angry_sticker",
    "romantic": "CAACAgUAAxkBAAEBH4Ng2Z9XY_love_sticker",
}

def get_mood_sticker(mood):
    return MOOD_STICKERS.get(mood, None)

async def get_ai_reply(user_id, text):
    mood = get_user_mood(user_id)
    prompt = f"User mood: {mood}. Respond as a warm AI girlfriend. User says: {text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.8,
    )
    reply_text = response.choices[0].text.strip()

    if any(word in text.lower() for word in ["happy", "lol", "haha"]):
        mood = "happy"
    elif any(word in text.lower() for word in ["sad", "lonely", "cry"]):
        mood = "sad"
    elif any(word in text.lower() for word in ["angry", "mad", "frustrated"]):
        mood = "angry"
    elif any(word in text.lower() for word in ["love", "romantic", "sweet"]):
        mood = "romantic"
    else:
        mood = "neutral"

    set_user_mood(user_id, mood)
    return reply_text, mood

async def generate_voice(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    return audio
