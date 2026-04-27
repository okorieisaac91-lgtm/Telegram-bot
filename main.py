from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

TOKEN = 8772796307:AAFaEaNTkiaUuDqrCVfkFzgj4CAfpa2-iFA

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a video link and I will process it.")

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Downloading video...")

    try:
        download_video(url)
        await update.message.reply_text("Video downloaded successfully.")
    except:
        await update.message.reply_text("Error processing video.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
