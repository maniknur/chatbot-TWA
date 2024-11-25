from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("Hello! Welcome to the Telegram Chatbot!")

if __name__ == "__main__":
    app = ApplicationBuilder().token("<YOUR_TELEGRAM_BOT_TOKEN>").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
