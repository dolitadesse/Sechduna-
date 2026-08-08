import os
import random

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ======================
# BOT TOKEN
# ======================
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# ======================
# ADMIN ID
# ======================
ADMIN_ID = 123456789

# ======================
# USER PRAYER MODE
# ======================
user_prayer_mode = {}

# ======================
# BIBLE VERSES
# ======================
verses = [
    "መዝሙር 23:1 - ጌታ እረኛዬ ነው፥ ምንም አይጎድልኝም።",
    "ዮሐንስ 3:16 - እግዚአብሔር ዓለምን እንዲህ ወደደ...",
    "ፊልጵስዩስ 4:13 - ሁሉን ነገር በሚያበረታኝ በክርስቶስ እችላለሁ።",
    "ሮሜ 8:28 - ሁሉም ነገር ለመልካም ይሰራል...",
]

# ======================
# CHURCH INFO
# ======================
church_name = "የሴች ዱና ቃለ ሕይወት ቤ/ክርስቲያን"
church_location = "Hosanna"
church_program = "እሁድ ከጠዋቱ 2:30 ጀምሮ"


# ======================
# START COMMAND
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        f"🙏 እንኳን ወደ {church_name} Bot በደህና መጣህ!\n\n"
        "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
        "👉 /church - የቤ/ክርስቲያን መረጃ\n"
        "👉 /pray - የጸሎት ጥያቄ\n"
        "👉 /help - መርጃ"
    )


# ======================
# VERSE COMMAND
# ======================
async def verse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    selected_verse = random.choice(verses)

    await update.message.reply_text(
        f"📖 {selected_verse}"
    )


# ======================
# CHURCH INFO COMMAND
# ======================
async def church(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

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
    if not update.message or not update.effective_user:
        return

    user_id = update.effective_user.id

    user_prayer_mode[user_id] = True

    await update.message.reply_text(
        "🙏 የጸሎት ጥያቄህን ጻፍ።"
    )


# ======================
# HELP COMMAND
# ======================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "🤖 የBot ትዕዛዞች\n\n"
        "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
        "👉 /church - የቤ/ክርስቲያን መረጃ\n"
        "👉 /pray - የጸሎት ጥያቄ\n"
        "👉 /help - መርጃ\n"
        "👉 /start - መጀመሪያ"
    )


# ======================
# AUTO REPLY
# ======================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.messageornotupdate.message.text:
                return

        user_id = update.effective_user.id
        text = update.message.text.strip().lower()


    # ======================
    # PRAYER REQUEST
    # ======================
        if user_prayer_mode.get(user_id):

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=(
                "🙏 አዲስ የጸሎት ጥያቄ\n\n"
                f"👤 ከ: {update.effective_user.full_name}\n\n"

                f"🆔 User ID: {user_id}\n\n"
                f"📝 ጥያቄ:\n{text}"
            ),
        )

        await update.message.reply_text(
            "✅ የጸሎት ጥያቄህ ተልኳል።\n🙏 እግዚአብሔር ይስማህ!"
        )

        user_prayer_mode[user_id] = False
        return

    # ======================
    # GREETING
    # ======================
    if any(word in text for word in ["hello", "hi", "ሰላም", "selam"]):

        await update.message.reply_text(
            f"ሰላም 😊\n"
            f"እንኳን ወደ {church_name} በደህና መጣህ!"
        )

    # ======================
    # HELP
    # ======================
    elif any(word in text for word in ["help", "እገዛ"]):

        await help_command(update, context)

    # ======================
    # VERSE
    # ======================
    elif "verse" in text or "መጽሐፍ" in text:

        selected_verse = random.choice(verses)

        await update.message.reply_text(
            f"📖 {selected_verse}"
        )

    # ======================
    # CHURCH INFO
    # ======================
    elif any(
        word in text
        for word in ["church", "ቤተክርስቲያን", "ቤ/ክርስቲያን"]
    ):

        await update.message.reply_text(
            f"⛪ {church_name}\n"
            f"📍 {church_location}\n"
            f"🕒 {church_program}"
        )

    # ======================
    # THANKS
    # ======================
    elif any(
        word in text
        for word in [
            "thanks",
            "thank you",
            "እግዚአብሔር ይባርክህ",
        ]
    ):

        await update.message.reply_text(
            "🙏 እግዚአብሔር ይባርክህ!"
        )

    # ======================
    # BYE
    # ======================
    elif any(
        word in text
        for word in ["bye", "goodnight"]
    ):

        await update.message.reply_text(
            "👋 ደህና ሁን! እግዚአብሔር ከአንተ ጋር ይሁን። 🙏"
        )


# ======================
# MAIN
# ======================
def main():
    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    # ======================
    # COMMAND HANDLERS
    # ======================
    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("verse", verse)
    )

    application.add_handler(
        CommandHandler("church", church)
    )

    application.add_handler(
        CommandHandler("pray", pray)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    # ======================
    # MESSAGE HANDLER
    # ======================
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            auto_reply
        )
    )

    print("🤖 Church Bot is running...")

    # python-telegram-bot v21.6
    application.run_polling()


# ======================
# RUN BOT
# ======================
if __name__ == "__main__":
    main()
