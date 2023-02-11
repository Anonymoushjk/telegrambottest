import logging
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "6236847085:AAEwZFAUmX1YBk53gPa-A9zc3uOzrb2iqpg"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    url = f"{BASE_URL}sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

def start(update, context):
    send_message(update["message"]["chat"]["id"], "Hi there! I'm a Telegram bot. Type /help for more information on what I can do.")

def help(update, context):
    send_message(update["message"]["chat"]["id"], "Here are the available commands:\n\n"
                                                                      "/start - Send a welcome message\n"
                                                                      "/help - Display a list of available commands\n"
                                                                      "/info - Display information about the bot\n"
                                                                      "/status - Display the current status of the bot\n")

def info(update, context):
    send_message(update["message"]["chat"]["id"], "I am a Telegram bot created with Python and the requests library. My purpose is to demonstrate how to create a simple Telegram bot.")

def status(update, context):
    send_message(update["message"]["chat"]["id"], "The bot is currently running and ready to receive commands.")

def handle_update(update):
    if "message" in update:
        message = update["message"]
        if "text" in message:
            text = message["text"]
            if text == "/start":
                start(update, None)
            elif text == "/help":
                help(update, None)
            elif text == "/info":
                info(update, None)
            elif text == "/status":
                status(update, None)

def main():
    offset = None
    while True:
        response = requests.get(f"{BASE_URL}getUpdates?offset={offset}").json()
        if response["ok"]:
            for update in response["result"]:
                handle_update(update)
                offset = update["update_id"] + 1

if __name__ == '__main__':
    main()
