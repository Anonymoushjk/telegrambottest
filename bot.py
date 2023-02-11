import telegram

# Replace with your API token
API_TOKEN = "your_api_token_here"

# Create a bot instance
bot = telegram.Bot(token=API_TOKEN)

def handle_message(bot, update):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    # Respond to the user's message
    bot.send_message(chat_id=chat_id, text="Received message: " + text)

# Start the bot
updater = telegram.Updater(token=API_TOKEN)
dispatcher = updater.dispatcher

# Add a handler for incoming messages
message_handler = telegram.MessageHandler(telegram.Filters.text, handle_message)
dispatcher.add_handler(message_handler)

# Start the updater
updater.start_polling()
