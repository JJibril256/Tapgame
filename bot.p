from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# -------------------------------
# EDIT THIS: Your live Web App URL
GAME_URL = "https://tapcoin-tkwt.onrender.com"
# -------------------------------

# Inline button for the Web App
def get_game_button():
    keyboard = [
        [InlineKeyboardButton("🎮 Play Tap Game", url=GAME_URL)]
    ]
    return InlineKeyboardMarkup(keyboard)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! Welcome to TapCoin game.\nClick the button below to start tapping!",
        reply_markup=get_game_button()
    )

# Set up the bot
if __name__ == "__main__":
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # <-- Replace with your bot token
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))

    print("Bot is running... Press CTRL+C to stop")
    app.run_polling()
``
