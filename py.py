from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_API_KEY' with your actual Telegram bot API key
API_KEY = '7661945650:AAFy5GsYZ2Wwf4Tg7PBRSDz2rDwqVYosJpA'

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    # Send an image with a "Join Community" button
    chat_id = update.message.chat_id
    image_url = 'https://raw.githubusercontent.com/maxscripts/bots/refs/heads/main/pawss.jpg'  # Replace with your image URL
    buttons = InlineKeyboardButton('Lets Go', url='https://t.me/dogsoghouse_bot/Dogs')  # Replace with your community link
    button = InlineKeyboardButton('Join dogs Community', url='https://t.me/dogs')  # Replace with your community link
    keyboard = InlineKeyboardMarkup([[buttons,button]])

    await context.bot.send_photo(chat_id=chat_id, photo=image_url, caption="How cool is your Telegram profile?\nCheck your rating and receive rewards 🦴", reply_markup=keyboard)

def main():
    # Create an Application object and pass your bot's API key
    application = Application.builder().token(API_KEY).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
