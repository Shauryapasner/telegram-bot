import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")  # Render Dashboard me Environment Variable me BOT_TOKEN set karna
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Dispatcher banate hain
dispatcher = Dispatcher(bot, None, workers=0)

# Start command
def start(update: Update, context):
    update.message.reply_text("👋 Hello! I am alive on Render!")

# Echo (jo bhi message bhejo, wahi wapas karega)
def echo(update: Update, context):
    update.message.reply_text(update.message.text)

# Handlers add karna
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is running on Render 🚀"
