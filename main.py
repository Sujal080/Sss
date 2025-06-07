from config import MASTER_TOKEN
from extractor import get_all_batches, get_txt_for_batch
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = "7460074981:AAH3xfM8LwbSaxqh9HMW_1QKfYXSHKZBRU0"

def start(update, context):
    update.message.reply_text("🎓 Welcome to RG Bot! Use /get_batches or /get_txt")

def get_batches(update, context):
    batches = get_all_batches()
    update.message.reply_text("\n".join(batches))

def get_txt(update, context):
    if len(context.args) == 0:
        update.message.reply_text("❗ Usage: /get_txt <batch_id>")
        return
    batch_id = context.args[0]
    txt = get_txt_for_batch(batch_id)
    update.message.reply_document(document=("batch.txt", txt))

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("get_batches", get_batches))
dp.add_handler(CommandHandler("get_txt", get_txt, pass_args=True))
updater.start_polling()
updater.idle()
