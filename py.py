from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, JobQueue
import asyncio

# Replace 'YOUR_API_KEY' with your actual Telegram bot API key
API_KEY = '7661945650:AAFy5GsYZ2Wwf4Tg7PBRSDz2rDwqVYosJpA'

# Function to send periodic updates
async def send_periodic_message(context: CallbackContext) -> None:
    chat_id = context.job.chat_id
    image_url = 'https://raw.githubusercontent.com/maxscripts/bots/refs/heads/main/pawss.jpg'
    buttons = InlineKeyboardButton('Lets Go', url='https://t.me/dogsoghouse_bot/Dogs')
    button = InlineKeyboardButton('Join dogs Community', url='https://t.me/dogs')
    keyboard = InlineKeyboardMarkup([[buttons, button]])

    await context.bot.send_photo(
        chat_id=chat_id,
        photo=image_url,
        caption="Periodic Update: Check your Telegram profile rating and earn rewards! 🦴",
        reply_markup=keyboard
    )

# Start command to register periodic tasks
async def start(update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text("You have subscribed to periodic updates!")

    # Add a periodic task to send updates every hour
    context.job_queue.run_repeating(send_periodic_message, interval=3600, first=0, chat_id=chat_id)

def main():
    application = Application.builder().token(API_KEY).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Use a background worker via the JobQueue
    job_queue = JobQueue()
    job_queue.set_application(application)
    job_queue.start()

    # Run the bot indefinitely
    asyncio.run(application.initialize())
    application.job_queue = job_queue
    application.start()
    application.idle()

if __name__ == '__main__':
    main()
