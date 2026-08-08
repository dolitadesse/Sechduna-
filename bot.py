import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.environ.get("BOT_TOKEN")

ADMIN_ID = 123456789
user_prayer_mode = {}

# ======================
# BIBLE VERSES
# ======================
verses = [
    "መዝሙር 23:1 - ጌታ እረኛዬ ነው፥ ምንም አይጎድልኝም።",
    "ዮሐንስ 3:16 - እግዚአብሔር ዓለምን እንዲህ ወደደ...",
    "ፊልጵስዩስ 4:13 - ሁሉን ነገር በሚያበረታኝ በክርስቶስ እችላለሁ።",
    "ሮሜ 8:28 - ሁሉም ነገር ለመልካም ይሰራል..."
]

# ======================
# CHURCH INFO
# ======================
church_name = "የሴች ዱና ቃለ ሕይወት ቤ/ክርስቲያን"
church_location = "hosanna"
church_program = "እሁድ ከጠዋቱ 2:30 ጀምሮ"

# ======================
# START
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🙏 እንኳን ወደ {church_name} Bot በደህና መጣህ!\n\n"
        "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
        "👉 /church - የቤ/ክርስቲያን መረጃ\n"
        "👉 /pray - የጸሎት ጥያቄ\n"
        "👉 /help - መርጃ"
    )

# ======================
# VERSE
# ======================
async def verse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    v = random.choice(verses)
    await update.message.reply_text(f"📖 {v}")

# ======================
# CHURCH INFO COMMAND
# ======================
async def church(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"⛪ {church_name}\n\n"
        f"📍 ቦታ: {church_location}\n"
        f"🕒 ፕሮግራም: {church_program}\n\n"
        "🙏 እግዚአብሔር ይባርካችሁ!"
    )

# ======================
# PRAY COMMAND
# ======================
async def pray(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_prayer_mode[user_id] = True

    await update.message.reply_text(
        "🙏 የጸሎት ጥያቄህን ጻፍ"
    )

# ======================
# AUTO REPLY
# ======================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()

    # ======================
    # PRAYER REQUEST SEND
    # ======================
    if user_prayer_mode.get(user_id):

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🙏 አዲስ የጸሎት ጥያቄ:\n\n{text}"
        )

        await update.message.reply_text(
            "✅ ጸሎት ጥያቄህ ተልኳል 🙏"
        )

        user_prayer_mode[user_id] = False
        return

    # ======================
    # GREETING
    # ======================
    if any(word in text for word in ["hello", "hi", "ሰላም", "selam"]):

        await update.message.reply_text(
            f"ሰላም 😊\nእንኳን ወደ {church_name} በደህና መጣህ!"
        )

    # ======================
    # HELP
    # ======================
    elif any(word in text for word in ["help", "እገዛ"]):

        await update.message.reply_text(
            "🤖 የBot ትዕዛዞች\n\n"
            "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
            "👉 /church - የቤ/ክርስቲያን መረጃ\n"
            "👉 /pray - የጸሎት ጥያቄ\n"
        )

    # ======================
    # VERSE
    # ======================
    elif "verse" in text or "መጽሐፍ" in text:

        v = random.choice(verses)
        await update.message.reply_text(f"📖 {v}")

    # ======================
    # CHURCH INFO
    # ======================
    elif any(word in text for word in ["church", "ቤተክርስቲያን"]):

        await update.message.reply_text(
            f"⛪ {church_name}\n📍 {church_location}\n🕒 {church_program}"
        )

    # ======================
    # THANKS
    # ======================
    elif any(word in text for word in ["thanks", "thank you", "እግዚአብሔር ይባርክህ"]):

        await update.message.reply_text(
            "🙏 እግዚአብሔር ይባርክህ!"
        )

    # ======================
    # BYE
    # ======================
    elif any(word in text for word in ["bye", "goodnight"]):

        await update.message.reply_text(
            "👋 ደህና ሁን!"
        )
