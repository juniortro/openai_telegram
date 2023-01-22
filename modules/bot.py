from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from modules.open_ai import send_response

TOKEN = os.getenv(key="TELEGRAM_KEY")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    response = send_response(message)
    
    await update.message.reply_text(response)

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.run_polling()