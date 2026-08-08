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
# ADMIN INFO
# ======================
ADMIN_ID = 417243779
ADMIN_USERNAME = "@Abd10t"


# ======================
# USER PRAYER MODE
# ======================
user_prayer_mode = {}


# ======================
# BIBLE VERSES
# ======================
verses = [
    "መዝሙር 23:1 - እግዚአብሔር እረኛዬ ነው፥ የሚያሳጣኝም የለም።",
    "ዮሐንስ 3:16 - በእርሱ የሚያምን ሁሉ የዘላለም ሕይወት እንዲኖረው እንጂ እንዳይጠፋ እግዚአብሔር አንድያ ልጁን እስኪሰጥ ድረስ ዓለሙን እንዲሁ ወዶአልና።",
    "ፊልጵስዩስ 4:13 - ኃይልን በሚሰጠኝ በክርስቶስ ሁሉን እችላለሁ።",
    "ሮሜ 8:28 - 28 እግዚአብሔርንም ለሚወዱት እንደ አሳቡም ለተጠሩት ነገር ሁሉ ለበጎ እንዲደረግ እናውቃለን።",
]


# ======================
# CHURCH INFO
# ======================
church_name = "Sech Duna ቃለ ሕይወት ቤተ ክርስቲያን"
church_location = "Hosanna"

church_program = (
    "📅 የሳምንቱ ፕሮግራሞች\n\n"
    "🙏 እሁድ - መደበኛ ፕሮግራም\n"
    "🕑 2:00 ሰዓት\n\n"
    "👥 ማክሰኞ - የወጣቶች ፕሮግራም\n"
    "🕚 11:00 ሰዓት\n\n"
    "👩 ረቡዕ - የእናቶች ፕሮግራም\n"
    "🕥 10:35 ሰዓት\n\n"
    "🙏 ሐሙስ - ፋውስ ፕሮግራም\n"
    "🕥 10:35 ሰዓት"
)


# ======================
# START COMMAND
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        f"🙏 እንኳን ወደ {church_name} Bot በደህና መጣህ!\n\n"
        "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
        "👉 /church - የቤተ ክርስቲያን መረጃ\n"
        "👉 /pray - የጸሎት ጥያቄ\n"
        "👉 /help - መርጃ\n"
        "👉 /myid - Telegram User ID"
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
        f"📍 ቦታ: {church_location}\n\n"
        f"{church_program}\n\n"
        "🙏 እንኳን ወደ ቃለ ሕይወት ቤተ ክርስቲያን Bot "
        "በደህና መጣችሁ!\n"
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
        "🙏 የጸሎት ጥያቄህን ጻፍ።\n\n"
        "ምሳሌ፦\n"
        "📝 ለቤተሰቤ እና ለስራዬ ጸሎት እፈልጋለሁ።"
    )


# ======================
# HELP COMMAND
# ======================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "🤖 የBot ትዕዛዞች\n\n"
        "👉 /start - መጀመሪያ\n"
        "👉 /verse - የመጽሐፍ ቅዱስ ጥቅስ\n"
        "👉 /church - የቤተ ክርስቲያን መረጃ\n"
        "👉 /pray - የጸሎት ጥያቄ\n"
        "👉 /help - መርጃ\n"
        "👉 /myid - Telegram User ID"
    )


# ======================
# MY ID COMMAND
# ======================
async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.effective_user:
        return

    user_id = update.effective_user.id

    await update.message.reply_text(
        f"🆔 Telegram User IDህ:\n\n{user_id}"
    )


# ======================
# AUTO REPLY
# ======================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    if not update.effective_user:
        return

    user_id = update.effective_user.id
    text = update.message.text.strip().lower()


    # ======================
    # PRAYER REQUEST
    # ======================
    if user_prayer_mode.get(user_id):

        prayer_text = update.message.text

        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=(
                    "🙏 አዲስ የጸሎት ጥያቄ\n\n"
                    f"👤 ከ: {update.effective_user.full_name}\n"
                    f"🆔 User ID: {user_id}\n\n"
                    f"📝 ጥያቄ:\n{prayer_text}"
                ),
            )

            await update.message.reply_text(
                "✅ የጸሎት ጥያቄህ ተልኳል።\n\n"
                "🙏 እግዚአብሔር ጸሎትህን ይስማ!\n"
                "❤️ ጌታ ከአንተ ጋር ይሁን።"
            )

        except Exception as error:
            print(f"❌ Admin message error: {error}")

            await update.message.reply_text(
                "⚠️ የጸሎት ጥያቄህን ለAdmin መላክ አልተቻለም።\n\n"
                "እባክህ እንደገና ሞክር።"
            )

        user_prayer_mode[user_id] = False
        return


    # ======================
    # GREETING
    # ======================
    if any(
        word in text
        for word in ["hello", "hi", "ሰላም", "selam"]
    ):
        await update.message.reply_text(
            f"ሰላም 😊\n"
            f"እንኳን ወደ {church_name} Bot በደህና መጣህ!"
        )


    # ======================
    # HELP
    # ======================
    elif any(
        word in text
        for word in ["help", "እገዛ"]
    ):
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
        for word in [
            "church",
            "ቤተክርስቲያን",
            "ቤ/ክርስቲያን",
        ]
    ):
        await update.message.reply_text(
            f"⛪ {church_name}\n\n"
            f"📍 {church_location}\n\n"
            f"{church_program}"
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
            "👋 ደህና ሁን! "
            "እግዚአብሔር ከአንተ ጋር ይሁን። 🙏"
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

    application.add_handler(
        CommandHandler("myid", myid)
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

    print("🤖 Sech Duna Church Bot is running...")

    # python-telegram-bot v21.6
    application.run_polling()


# ======================
# RUN BOT
# ======================
if __name__ == "__main__":
    main()
