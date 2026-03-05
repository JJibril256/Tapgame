from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8760944060:AAEukMQtGe2274nt0f9JryJ2bE_422hBpHo"  # Replace with BotFather token
GAME_URL = "http://127.0.0.1:5000"  # Use local URL first for testing

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚀 Play Tap Game", web_app=WebAppInfo(url=GAME_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to TapCoin!\nTap coins and earn rewards.", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
