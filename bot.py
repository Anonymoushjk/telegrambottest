import os

from anydlbot import AnyDLBot

bot = AnyDLBot(token=os.environ['6236847085:AAEwZFAUmX1YBk53gPa-A9zc3uOzrb2iqpg'])


@bot.command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! How can I help you today?")


@bot.command
def download(update, context):
    file_url = context.args[0]
    file_name = context.args[1] if len(context.args) > 1 else None

    file = bot.download(file_url, file_name)

    context.bot.send_document(chat_id=update.message.chat_id, document=file)

if __name__ == "__main__":
    bot.run()
