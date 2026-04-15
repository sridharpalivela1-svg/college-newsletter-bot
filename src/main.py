import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database.models import SessionLocal, User
from database.init_db import setup_database
from services.newsletter_generator import generate_personalized_newsletter

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = SessionLocal()
    user = User(chat_id=update.effective_chat.id, college="ACET", program="DS-C")
    session.merge(user)
    session.commit()
    session.close()
    await update.message.reply_text("Subscribed!")

async def newsletter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = SessionLocal()
    user = session.query(User).filter_by(chat_id=update.effective_chat.id).first()
    if user:
        await update.message.reply_text("🤖 Generating...")
        text = generate_personalized_newsletter(user)
        await update.message.reply_text(text)
    session.close()

if __name__ == '__main__':
    os.makedirs('/app/data', exist_ok=True)
    setup_database()
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newsletter", newsletter))
    app.run_polling()
