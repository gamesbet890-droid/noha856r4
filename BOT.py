from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram Bot Token
TOKEN = "9113822945:AAE1BdgaQBuTOLVnKnkPUm9DRR-qa99mUEo"

# 1. Path to your image inside the local folder
IMAGE_PATH = "images/welcome.jpg"

# 2. Welcome caption in Amharic
WELCOME_CAPTION = (
    "🎰 *እንኳን ወደ Betgames በደህና መጡ!* 🚀\n\n"
    "ለአዳዲስ አባሎቻችን ልዩ ስጦታ አዘጋጅተናል!\n\n"
    "🎁 *የ 50% ቦነስ + 100 ብር ተጨማሪ ቦነስ* አሁኑኑ ያግኙ!\n\n"
    "👇 ለመጀመር ከታች ያለውን ይጫኑ እና መጫወት ይጀምሩ!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Action buttons
    keyboard = [
        [InlineKeyboardButton("🎮 አሁኑኑ ተመዝገብ (Register)", url="https://t.me/LuckyFlip_gamebot")],
        [InlineKeyboardButton("🎁 ቦነስ ውሰድ (Claim Bonus)", callback_data="claim_bonus")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Open local image file and send it with the caption
    with open(IMAGE_PATH, 'rb') as photo_file:
        await update.message.reply_photo(
            photo=photo_file,
            caption=WELCOME_CAPTION,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()